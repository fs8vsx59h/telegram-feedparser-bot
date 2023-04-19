import feedparser
import asyncio


async def async_dmhy_parse(url):
  loop = asyncio.get_event_loop()
  rss_content = await loop.run_in_executor(None, feedparser.parse, url)
  link_list = []
  for entry in rss_content.entries:
    if 'href' in entry.links[1]:
      link_list.append(entry.links[1].href)
  return link_list


async def test():
  url = 'https://dmhy.org/topics/rss/rss.xml?keyword=%E7%A9%BA%E4%B9%8B%E5%A2%83%E7%95%8C'
  result = await async_dmhy_parse(url)
  print(result)


if __name__ == "__main__":
  asyncio.run(test())
