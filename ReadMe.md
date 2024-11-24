# ReadMe

* Are you using [Dynamic Prompts](https://github.com/adieyal/sd-dynamic-prompts) and use a complex structure of multiple directories and dozens of files?
* Are you tired of seeing errors refering to missing ``{}`` or ``__`` without any idea where to look for?

This is for you!

This checks for matching:
* ``{}``
* ``__``
* And verifies that ``{{x-y$$ <sep> $$<strings>}}`` has double-braces!

Just place this script in your projects root directory and let it run.

It'll report any mismatch with filename and line number!

You're welcome :)
