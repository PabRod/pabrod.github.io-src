Title: There's a nerd in my elevator!
Date: 5/1/2018, 12:24:00 PM
Category: Blog
Lang: en
Tags: physics, python
Slug: elevator
Authors: Pablo Rodríguez-Sánchez
Summary: An elevator, a phone, ... and a nerd
Comments: True

_This text appeared first in [Naukas](http://fuga.naukas.com/2018/02/06/un-empollon-en-mi-ascensor/), where was originally written in Spanish._

Recently I started a secondment at the Friedrich Schiller University, in Jena, Germany. Surprisingly, my office during the next months is located in the 18th floor of a skyscrapper. The Jentower in particular:

![Jentower](http://fuga.naukas.com/files/2018/02/2018-01-30-16.34.25-360x640.jpg)

But I'm not writing this to boast about the views of my new office. On the contrary, I'll destroy any possible idea of glamour related to work in a place like this. And I'll do it with a confession: I became the crazy guy who leaves his cell phone on the ground while he uses the elevator. Let me explain:

A building of almost 150 meters high needs fast elevators. The ones in this building have a very powerful, scary acceleration. Then, I remembered that smartphones usually contain an accelerometer, so I tried to measure those accelerations.

I used an app called [Google Science Journal](https://sciencejournal.withgoogle.com), that allows registering data from all sensors avaible in the phone (accelerometers, light, magnetic field, ...) and export them in a format (.csv) quite easy to analyze on a computer. If you like getting your hands dirty, install it now!

In the figure below we can see the vertical acceleration profile during my trip to the 18th floor this morning, where we can clearly see the initial "kick" (seconds 9 to 14) and the braking (28 to 33)

![accel](http://fuga.naukas.com/files/2018/02/acel1-580x391.png)
Vertical acceleration (excluding gravity)

Accelerations of 1 m/s^2 sustained during 4 seconds! You can feel that in your stomach!

Using this data, we can explore a bit further. We can use a time series of the acceleration to compute speed and position. How? Maybe you remember from high school's physics that position, speed and acceleration are related through derivatives. More specifically.

![diff](http://fuga.naukas.com/files/2018/02/diff.png)

With the previous recipe we can compute speed using the position, and then use speed to compute acceleration. Like in a production chain. Nevertheless, in our case we want to do the opposite process. Luckily, we can use indefinite integrals to "revert" our derivatives, and thus our whole "production chain".

![int](http://fuga.naukas.com/files/2018/02/int.png)

So, by integrating the acceleration (to obtain the speed), and then integrating the speed (to obtain the position) we find results like this:

![results](http://fuga.naukas.com/files/2018/02/all-580x564.png)
Acceleration, speed and position

So, using only a device that most of us carry everywhere and some elementary physical concepts we know that:

- Our elevator runs up at 4 m/s.
- My office is 74 meter above the ground.

Such a great time to be a nerd!

If someone is interested in exploring a bit deeper into the details (for instance: how to filter out the effects of gravity, how to integrate a time series, ... ) or even experiment with his or her own elevator, [here is a link](https://github.com/PabRod/elevator-tool) to the code I've used.
