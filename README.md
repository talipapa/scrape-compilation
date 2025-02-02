# Project documentation

### Common commands
> Suppose that [] is a template

Create venv for windows 11
```bash
1. virtualenv [name_of_env]
2. source [name_of_env]/Scripts/activate
```

Create scrapy project
```bash
scrapy startproject [project_name]
```

Pioneering the website using scrapy shell
```bash
scrapy shell [link_of_website_to_scrape]
```
or
```bash
scrapy shell

> fetch(link_of_website_to_scrape)
```

Create new spider
```bash
scrapy genspider [name_of_spider]
```

Run the crawl
```bash
scrapy crawl [name_of_spider]
```
