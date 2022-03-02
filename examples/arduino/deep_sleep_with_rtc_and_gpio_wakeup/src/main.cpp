/* 
  Author: Nigel Bajema
  Created: March 1 2022

  This example demonstrates using the RTC alarm and GPIO interrupt
  to wake the Apollo3 from deep sleep.
  It was created from the following Sparkfun Examples 
  from version 2.2.0 of this repo: https://github.com/sparkfun/Arduino_Apollo3

    * RTC/Example6_LowPower_Alarm
    * Apollo3/Example8_AttachInterrupt

  Original copyright headers below:
*/

/*
  Author: Adam Garbo and Nathan Seidle
  Created: June 3rd, 2020

  This example demonstrates how to set an RTC alarm and enter deep sleep.

  The code is configured to set an RTC alarm every minute and enter
  deep sleep between interrupts. The RTC interrupt service routine will
  wake the board and print the date and time upon each alarm interrupt.

  Tested with a SparkFun Edge 2. Confirmed sleep current of 2.5 uA.
*/

/*
// This file is subject to the terms and conditions defined in
// file 'LICENSE.md', which is part of this source code package.
*/

//The Software License mentioned above (LICENSE.md)  is as follows:

/*
  Copyright (c) 2020 SparkFun Electronics

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
*/

#include "Arduino.h"
#include "RTC.h"

#define INT_PIN 19
#define MY_LED_PIN 5


volatile uint32_t count = 0;
uint32_t loop_count = 0;
bool alarmFlag = false;

void goToSleep();
void wakeUp();
void printDateTime();

void myISR(void){
  count++;
}

extern "C" void am_rtc_isr(void)
{
  // Clear the RTC alarm interrupt.
  rtc.clearInterrupt();

  // Set alarm flag
  alarmFlag = true;
}

void setup()
{
  Serial.begin(115200);

  rtc.setToCompilerTime();
  rtc.getAlarm();

  printf("Apollo3 - attachInterrupt\n\n");

  pinMode(MY_LED_PIN, OUTPUT);

  digitalWrite(MY_LED_PIN, LOW);

  rtc.setTime(0, 50, 59, 12, 3, 6, 20); // 12:59:50.000, June 3rd, 2020 (hund, ss, mm, hh, dd, mm, yy)

  // Set the RTC's alarm
  rtc.setAlarm(0, 0, 0, 13, 3, 6); // 13:00:00.000, June 3rd (hund, ss, mm, hh, dd, mm). Note: No year alarm register
  rtc.setAlarmMode(6);
  rtc.attachInterrupt();


}


void loop()
{
  pinMode(INT_PIN, INPUT_PULLUP);
  loop_count++;
  printDateTime();
  printf("time (ms): %d, count: %d, expected: %d, alarm: %s\r\n", millis(), count, loop_count, alarmFlag?"True":"False");
  Serial.println();
  Serial.println();

  digitalWrite(MY_LED_PIN, loop_count%2);
  delay(1000);
  attachInterrupt(INT_PIN, myISR, RISING);
  goToSleep();

}

void goToSleep()
{
  alarmFlag = false;
  // Disable UART
  Serial.end();

  // Disable ADC
  powerControlADC(false);

  // Force the peripherals off
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_IOM0);
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_IOM1);
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_IOM2);
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_IOM3);
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_IOM4);
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_IOM5);
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_ADC);
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_UART0);
  am_hal_pwrctrl_periph_disable(AM_HAL_PWRCTRL_PERIPH_UART1);

  // Disable all pads (except UART TX/RX)
  for (int x = 0 ; x < 50 ; x++)
  {
    switch(x)
    {
      case INT_PIN:
      case MY_LED_PIN:
        break;
      default:
        am_hal_gpio_pinconfig(x, g_AM_HAL_GPIO_DISABLE);
        break;
    }

  }

  //Power down CACHE, flashand SRAM
  am_hal_pwrctrl_memory_deepsleep_powerdown(AM_HAL_PWRCTRL_MEM_ALL); // Turn off CACHE and flash
  // am_hal_pwrctrl_memory_deepsleep_retain(AM_HAL_PWRCTRL_MEM_SRAM_384K); // Retain all SRAM (0.6 uA)
  am_hal_pwrctrl_memory_deepsleep_retain(AM_HAL_PWRCTRL_MEM_SRAM_64K_DTCM);

  // Keep the 32kHz clock running for RTC
  am_hal_stimer_config(AM_HAL_STIMER_CFG_CLEAR | AM_HAL_STIMER_CFG_FREEZE);
  am_hal_stimer_config(AM_HAL_STIMER_XTAL_32KHZ);

  am_hal_sysctrl_sleep(AM_HAL_SYSCTRL_SLEEP_DEEP); // Sleep forever

  // And we're back!
  wakeUp();
}

// Power up gracefully
void wakeUp()
{

  // Go back to using the main clock
  am_hal_stimer_config(AM_HAL_STIMER_CFG_CLEAR | AM_HAL_STIMER_CFG_FREEZE);
  am_hal_stimer_config(AM_HAL_STIMER_HFRC_3MHZ);

  // Power up SRAM, turn on entire Flash
  am_hal_pwrctrl_memory_deepsleep_powerdown(AM_HAL_PWRCTRL_MEM_MAX);

  // Go back to using the main clock
  am_hal_stimer_config(AM_HAL_STIMER_CFG_CLEAR | AM_HAL_STIMER_CFG_FREEZE);
  am_hal_stimer_config(AM_HAL_STIMER_HFRC_3MHZ);

  // Renable UART0 pins
  am_hal_gpio_pinconfig(48, g_AM_BSP_GPIO_COM_UART_TX);
  am_hal_gpio_pinconfig(49, g_AM_BSP_GPIO_COM_UART_RX);

  // Renable power to UART0
  am_hal_pwrctrl_periph_enable(AM_HAL_PWRCTRL_PERIPH_UART0);

  // Enable ADC
  initializeADC();

  detachInterrupt(INT_PIN);
  pinMode(INT_PIN, INPUT);
  // Enable Serial
  Serial.begin(115200);
  digitalWrite(LED_BUILTIN, (digitalRead(LED_BUILTIN)) ? LOW : HIGH); 
}

void printDateTime()
{
  rtc.getTime();
  Serial.printf("20%02d-%02d-%02d %02d:%02d:%02d.%03d\r\n",
                rtc.year, rtc.month, rtc.dayOfMonth,
                rtc.hour, rtc.minute, rtc.seconds, rtc.hundredths);
}
