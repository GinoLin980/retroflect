# Retroflect

*Bust through UWP loopback restrictions by reflecting outbound network traffic with GUI.*

An user-friendly app forked from [twisteroidambassador/retroflect](https://github.com/twisteroidambassador/retroflect) Python version.

## Why this is made?

I built a [Forza Horizon Realistic Gearbox](https://github.com/GinoLin980/Forza-Horizon-realistic-gearbox), and some people reported that the game from Microsoft Store doesn't work with it.

So after long time of research, it was a problem called `UWP Loopback Restrictions`, which means **Microsoft blocks the apps from communicating to Localhost.**

I found Twisteroid's Retroflect project solved this problem the best, how wonderful. With the simple code he/she have written, it's easy to twist variables and take use of it.

**But it seems a bit hard for normal people who will use it frequently.** Therefore this fork was made.

And it was pulled out as an independent project because there are more apps can use it rather than only my Realistic Gearbox.

## Features

### Ping Tool:

* Retroflect requires an unused IP, but it would be hard for a normal person to know what IP is in used or not.

  So a ping tool is built in app.

### IP List:

* For those who will use Retroflect frequently, manually entering the IP would be annoying.

  Not a problem anymore! The unused IPs will be saved in a list after you pinged it.

## Instructions

1. Open `Ping.and.Retroflect.Utility.exe with Administrator.`
2. Choose unused IP and ping it. (Five commonly unused IPs are listed in app)
3. If the IP is unused, it will be saved to the option menu below.
4. Choose a IP and click `Retroflect`.
5. Configure the data sending app(server) to `<IP YOU CHOSE TO RUN RETROFLECT>` and port to `8000`
6. Configure the data receiving app(client) to `0.0.0.0:8000`.
7. DONE!!!
