## Multi tread simple HTTP testing tool

This is a test tool for creating a flood of GET HTTP requests to check web-host capabilities.
Originally created for testing WordPress installation on Azure VMs.

Multithreading powered by "concurrent.futures" and "ThreadPoolExecutor" particularly.



### How to use

```markdown
http-test.py testUrl numberOfRequests max_workers getRequestTimeout

# Parameters
- testUrl - test address, like "https://github.com/"
- numberOfRequests - how many requests in total will be send
- max_workers - number of parallel requests (threads)
- getRequestTimeout - connection timeout


**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/ivshof/HTTP-tester/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
