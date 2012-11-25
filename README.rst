=============================
555 Timer Component Optimizer
=============================

Allows users to calculate the optimal electronic components to
select for desired 555 timer circuit behavior.

There are many timers available on the web for calculating the
behavior characteristics of 555 timer circuits, but these do
not take into consideration the solution of these equations with
a particular desired behavior and constrained, available set of
components.

This package performs simple optimization to achieve a timing
circuit as close to the desired behavior as possible using a
defined set of electronic components.

Note: At the moment only astable circuits are supported
http://en.wikipedia.org/wiki/555_timer_IC#Astable

Usage
=====

Timing behaviors are solved by time high and time low rather than simple
frequency alone.


Mode 1: Set Pool of Available Components
----------------------------------------

This method is meant for selecting from a set of available components to
best fit/achieve a particular timing behavior.

.. code-block:: python

  from optimize_555.opt import optimize
  target_high = 42 #42 seconds
  target_low = 15 #15 seconds
  R1,R2,C,time_high,time_low = optimize(target_high, target_low)

`optimize` also accepts explicitly defined sets of resistors and capacitors through
parameters called `R_set` and `C_set`.

.. code-block:: python

  from optimize_555.opt import optimize_free
  target_high = 42 #42 seconds
  target_low = 15 #15 seconds
  R_set = [100, 1e3, 10e3, 1e6]
  R1,R2,C,time_high,time_low = optimize_free(target_high, target_low, R_set=R_set)

The above example defines 4 possible resistors values. The `R_set` and `C_set` lists
should be ordered for proper optimization.


Mode 2: Absolute Limits on Component Range
------------------------------------------

This method is meant for identifying a specific set of values for a particular
timing behavior within some range of allowable values. The exact components will
be procurred or constructed later.

.. code-block:: python

  from optimize_555.opt import optimize_free
  target_high = 42 #42 seconds
  target_low = 15 #15 seconds
  R1,R2,C,time_high,time_low = optimize_free(target_high, target_low)

optimize_free also takes a set of optional parameters `R_range` and `C_range`, which define
the minimum and maximum values for resistors and capacitors. For example to explicitly define
a resistor value range between 100 Ohms and 1 MOhm.

.. code-block:: python

  R_range = (100, 1e6)
  R1,R2,C,time_high,time_low = optimize_free(target_high, target_low, R_range, C_range)


DISCLAIMER
==========

I take no responsibility for fried circuits, toxic fumes inhaled by burning out
components, hurt feelings, broken dreams, or anything else that may happen
through the use of this application.

Use of this software is done at your own risk. I make no warranties about the
software's quality, performance, and accuracy.

Notes
=====

On brute force optimization
---------------------------

Most of the minimization functions that exist within scipy's optimization
module do not strictly respect bounded optimization. Overreaching bounds
in this problem could result in undesired capacitor values or even negative
numbers. The problem space itself is not all that large and can therefore easily
be crunched by brute force.

TODO
====

* More optimization options
* Real Integer Programming support
* Memoization?
* Web interface for demos
* SI unit support
