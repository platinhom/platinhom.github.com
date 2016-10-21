<section class="comment">
{% if layout.comment or page.comment %}
	{% if site.disqus.config %}
	<div id="disqus_thread"></div>
	<script type="text/javascript">
		//disqus,will affect the share contents above..
		var disqus_shortname = '{{ site.disqus.id }}';
		(function() {
			var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
			dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
			(document.getElementsByTagName('head')[0] ||
				document.getElementsByTagName('body')[0]).appendChild(dsq);
		})();
	</script>
	{% else %} 
		{% if site.duoshuo.config %}
		<div class="ds-share" data-thread-key="{{page.id}}" data-title="{{page.title}}" data-images="此处请替换为分享时显示的图片的链接地址" data-content="此处请替换为分享时显示的内容" data-url="{{ site.url }}{{ page.url | remove:'index.html' }}">
	     <div class="ds-share-inline">
	      <ul  class="ds-share-icons-16">
	      	<li data-toggle="ds-share-icons-more"><a class="ds-more" href="javascript:void(0);">分享到：</a></li>
	        <li><a class="ds-weibo" href="javascript:void(0);" data-service="weibo">微博</a></li>
	        <li><a class="ds-qzone" href="javascript:void(0);" data-service="qzone">QQ空间</a></li>
	        <li><a class="ds-qqt" href="javascript:void(0);" data-service="qqt">腾讯微博</a></li>
	        <li><a class="ds-wechat" href="javascript:void(0);" data-service="wechat">微信</a></li>
	      </ul>
	      <div class="ds-share-icons-more"></div>
	     </div>
	    </div>

		<div class="ds-thread" data-thread-key="{{page.id}}" data-title="{{page.title}}" data-url="{{ site.url }}{{ page.url | remove:'index.html' }}"></div>
			<script type="text/javascript">
			var duoshuoQuery = {short_name:"{{ site.duoshuo.id }}"};
				(function() {
					var ds = document.createElement('script');
					ds.type = 'text/javascript';ds.async = true;
					//ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
					ds.src='/jcss/js/embed.js';
					ds.charset = 'UTF-8';
					(document.getElementsByTagName('head')[0]
					 || document.getElementsByTagName('body')[0]).appendChild(ds);
				})();
			</script>
		{% endif %}
	{% endif %}
{% endif %}

{% if site.baiduShare.config %}
	<script>
		window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"1","bdSize":"16"},"share":{},"image":{"viewList":["weixin","douban","tsina","tqq","renren","mail"],"viewText":"分享到：","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["weixin","douban","tsina","tqq","renren","mail"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];
	</script>
{% endif %}
</section>
