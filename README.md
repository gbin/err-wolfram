# err-wolfram

This is a plugin for errbot so you can ask silly questions to [Wolfram Alpha](https://www.wolframalpha.com).

For example:

```
[@gbin ➡ @err] >>> !wa area of the sun / area of a penny
[@gbin ➡ @err] [␍]

2.1×10^22
```

You can install it by saying `!repos install https://github.com/gbin/err-wolfram` to the bot as an admin.
You need to configure the plugin before beeing able to use it with an API key you can get for free from Wolfram.

(replace the token with a valid one).
```
!plugin config Wolfram {'WA_TOKEN': '49UVXJ-VPL9XLVKAH'}
```

If the bot has not the right to install dependencies, you will need to do a `pip -r requirements.txt` yourself.