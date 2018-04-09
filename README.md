# atolye15-2018
Atölye15 - Staj Kampı 2018 Çalışmalar


## ls
This program is inpired from original `ls` in Linux Bash command line. I build small replica of it with basic parameters.
`-l` Shows detailed list with permissions, owner, size, time and name of course.
`-t` List files depending on their last modified oldest at the top.
`-s` List files depending on their size with descending order.
`-a` List all files including secret ones that has dot(.) in their first letter.
`-u` List files depending on their last read time, older at the top.

## sitemap
This script is unefficiently written sitemapper. It goes into the url given. Searches for new urls and pages and follows that, too. Unless they're external links or the ling count is bigger than 500.
In the beginning of the program `url` variable is the url that will be searched.
