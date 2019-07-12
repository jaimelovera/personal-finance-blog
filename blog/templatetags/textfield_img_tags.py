import os
from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def textfield_img_tags(value, post):
	if post.inline_image_1:
		value = value.replace("<img1>", "<img src="+static("blog/img/"+os.path.basename(post.inline_image_1.url))+">")
	if post.inline_image_2:
		value = value.replace("<img2>", "<img src="+static("blog/img/"+os.path.basename(post.inline_image_2.url))+">")
	if post.inline_image_3:
		value = value.replace("<img3>", "<img src="+static("blog/img/"+os.path.basename(post.inline_image_3.url))+">")
	if post.inline_image_4:
		value = value.replace("<img4>", "<img src="+static("blog/img/"+os.path.basename(post.inline_image_4.url))+">")
	if post.inline_image_5:
		value = value.replace("<img5>", "<img src="+static("blog/img/"+os.path.basename(post.inline_image_5.url))+">")
	if post.inline_image_6:
		value = value.replace("<img6>", "<img src="+static("blog/img/"+os.path.basename(post.inline_image_6.url))+">")
	return value
