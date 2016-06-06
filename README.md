# ![logo](https://raw.githubusercontent.com/villasv/plugandpie/master/docs/icon.png) Plug N Pie [![Build Status][bs]][ci] [![Code Quality][cq]][ci] [![Code Coverage][cc]][ci] [![Chat Room][chat-image]][chat-link] [![Documentation Status][docs-image]][docs-link]

### Installation
Requires `python-smbus` for Python 3
https://procrastinative.ninja/2014/07/21/smbus-for-python34-on-raspberry/


Workaround for repeated starts on Raspberry Pi i2c driver:
```
sudo su -
echo -n 1 > /sys/module/i2c_bcm2708/parameters/combined
exit
```

### Goal
```
>>> import plugandpie as pnp
>>> pnp.accelerometer.get_ms2()
{'x': 0.12, 'y': 1.14, 'z': 9.23}
```

[ci]: https://scrutinizer-ci.com/g/villasv/plugandpie/?branch=master
[bs]: https://scrutinizer-ci.com/g/villasv/plugandpie/badges/build.png?b=master
[cq]: https://scrutinizer-ci.com/g/villasv/plugandpie/badges/quality-score.png?b=master
[cc]: https://scrutinizer-ci.com/g/villasv/plugandpie/badges/coverage.png?b=master
[chat-image]: https://badges.gitter.im/villasv/plugandpie.svg
[chat-link]: https://gitter.im/villasv/plugandpie?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[docs-image]: http://plugpie.readthedocs.io/en/latest/?badge=latest
[docs-link]: https://readthedocs.org/projects/plugpie/badge/?version=latest