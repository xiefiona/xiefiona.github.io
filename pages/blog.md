---
layout: page
title: Blog
permalink: /blog/
---

<ul>
{% for post in site.posts %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> — <span class="post-date">{{ post.date | date: '%b %e, %Y' }}</span></li>
{% endfor %}
</ul>
