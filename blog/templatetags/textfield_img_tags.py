from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def textfield_img_tags(value, post):
	if post.inline_image_1:
		value = value.replace("<img1>", "<div class='box-image-container'><img class='box-image' onload='fadeImageIn(this);'' src=" + post.inline_image_1.url + " alt='Posts Image'></div>")
	if post.inline_image_2:
		value = value.replace("<img2>", "<div class='box-image-container'><img class='box-image' onload='fadeImageIn(this);'' src=" + post.inline_image_2.url + " alt='Posts Image'></div>")
	if post.inline_image_3:
		value = value.replace("<img3>", "<div class='box-image-container'><img class='box-image' onload='fadeImageIn(this);'' src=" + post.inline_image_3.url + " alt='Posts Image'></div>")
	if post.inline_image_4:
		value = value.replace("<img4>", "<div class='box-image-container'><img class='box-image' onload='fadeImageIn(this);'' src=" + post.inline_image_4.url + " alt='Posts Image'></div>")
	if post.inline_image_5:
		value = value.replace("<img5>", "<div class='box-image-container'><img class='box-image' onload='fadeImageIn(this);'' src=" + post.inline_image_5.url + " alt='Posts Image'></div>")
	if post.inline_image_6:
		value = value.replace("<img6>", "<div class='box-image-container'><img class='box-image' onload='fadeImageIn(this);'' src=" + post.inline_image_6.url + " alt='Posts Image'></div>")
	return value