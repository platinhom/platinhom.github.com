---
title: 归档
layout: page_small
---

<ul class="listing">
{% for post in site.posts %}
  {% if post.archive %}
  <li class="listing-item">
  <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
  <a href="{{ post.url }}" target='_blank' title="{{ post.title }}">{{ post.title }}</a>
  </li>
  {% endif %}
{% endfor %}
</ul>