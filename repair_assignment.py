from pathlib import Path


ROOT = Path(__file__).parent / "html_advanced"


def page(title: str, body: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="description" content="Techium is a digital agency">
    <link rel="icon" type="image/x-icon" href="./favicon.ico">
    <link rel="icon" type="image/png" href="./favicon.png">
    <title>{title}</title>
  </head>
  <body>
{body}
  </body>
</html>
'''


def write(name: str, content: str) -> None:
    (ROOT / name).write_text(content, encoding="utf-8")


nav = '''<nav><ul>
<li><a href="/">Home</a></li>
<li><a href="#services">Services</a></li>
<li><a href="#works">Works</a></li>
<li><a href="about.html">About</a></li>
<li><a href="latest_news.html">Latest news</a></li>
<li><a href="#testimonials">Testimonials</a></li>
<li><a href="contact.html">Contact</a></li>
</ul></nav>'''

social = '''<div><ul>
<li><a href="https://www.facebook.com/HolbertonSchool/">Facebook</a></li>
<li><a href="https://twitter.com/holbertonschool">Twitter</a></li>
<li><a href="https://www.instagram.com/holbertonschool/">Instagram</a></li>
</ul></div>'''

secondary = '''<div><ul>
<li><a href="#">Terms of Use</a></li>
<li><a href="#">Privacy Policy</a></li>
<li><a href="#">Cookie Policy</a></li>
</ul></div>'''

sections = '''<section id="hero"><header><h2>We help you build your brand!</h2></header><div><a href="#">Get started</a></div></section>
<section id="services"><header><h2>Services</h2><p>We work with you</p></header><div>
<h3><a href="#">Design &amp; Concept</a></h3><h3><a href="#">Digital Strategy</a></h3><h3><a href="#">Content Strategy</a></h3><h3><a href="#">UX Design</a></h3><h3><a href="#">Web Development</a></h3><h3><a href="#">Social Media</a></h3></div></section>
<section id="works"><header><h2>Works</h2><p>Take a look in our portfolio</p></header><div>
<article><h3><a href="#">Interior Design</a></h3></article><article><h3><a href="#">Web Development</a></h3></article><article><h3><a href="#">Personal Brand</a></h3></article></div></section>
<section id="about"><header><h2>About Us</h2><p>Everything about us</p></header><div>
<h3>Who are we</h3><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p>
<h3>Our culture</h3><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p>
<h3>How we work</h3><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p>
<a href="about.html">Learn more about us</a></div></section>
<section id="latest_news"><header><h2>Latest news</h2></header><div>
<article><p>Career</p><h3><a href="#">Hoc loco tenere se Triarius non potuit.</a></h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Id Sextilius factum negabat. Quo tandem modo? At eum nihili facit; Quae contraria sunt his, malane?</p><small>By Kelly D.</small></article>
<article><p>Digital Life</p><h3><a href="#">Ut alios omittam, hunc appello, quem ille unum secutus est.</a></h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Tum mihi Piso: Quid ergo? Tum ille: Ain tandem? Non autem hoc: igitur ne illud quidem. Sed quod proximum fuit non vidit. Nos commodius agimus. An nisi populari fama?</p><small>By William A.</small></article>
<article><p>Social</p><h3><a href="#">Bestiarum vero nullum iudicium puto.</a></h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Non igitur bene. Quid enim est a Chrysippo praetermissum in Stoicis? Pugnant Stoici cum Peripateticis. Prioris generis est docilitas, memoria; Apparet statim, quae sint officia, quae actiones.</p><small>By Frances J.</small></article></div></section>
<section id="testimonials"><header><h2>Testimonials</h2><p>We are more than a digital company</p></header><div>
<article><blockquote>I am completely blown away. Thanks to Techium, we've just launched our 5th website! <cite>Yuri Y.</cite></blockquote></article>
<article><blockquote>Thank you so much for your help. Techium company is awesome! <cite>Dorrie S.</cite></blockquote></article>
<article><blockquote>I love your system. Definitely worth the investment. I'd be lost without Techium company. <cite>Sven H.</cite></blockquote></article></div></section>
<section id="contact"><header><h2>Contact</h2><p>We like to know new people</p></header><div><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Id Sextilius factum negabat. Quo tandem modo? At eum nihili facit; Quae contraria sunt his, malane?</p><a href="contact.html">Get in touch</a></div></section>'''

header = f'''<header><div><a href="/"><span>Techium</span></a></div>{nav}</header>'''
footer = f'''<footer><div><img src="logo-black.png" alt="Techium logo" width="160" height="40"></div><address>234 Washington Street<br>Urbana, Illinois</address>{social}{secondary}</footer>'''

write("11-styleguide.html", page("Styleguide - Techium", '''<header></header><main><section><header><h2>Headings</h2></header><h1>Heading level 1</h1><h2>Heading level 2</h2><h3>Heading level 3</h3><h4>Heading level 4</h4><h5>Heading level 5</h5><h6>Heading level 6</h6></section></main><footer></footer>'''))
write("15-index.html", page("Homepage - Techium", f'''<header><div><span>Techium</span></div><nav></nav></header><main><h1>Homepage</h1>{sections}</main><footer><div>Footer</div></footer>'''))
write("16-index.html", page("Homepage - Techium", f'''<header><div><a href="/"><span>Techium</span></a></div>{nav}</header><main><h1>Homepage</h1>{sections}</main><footer><div>Footer</div></footer>'''))

comments = '''<!-- Header to help with scanning your code -->
<header><div><a href="/"><span>Techium</span></a></div>''' + nav + '''</header>
<!-- Main to help with scanning your code -->
<main><h1>Homepage</h1>
<!-- Hero section -->
<section><header><h2>We help you build your brand!</h2></header><div><a href="#">Get started</a></div></section>
<!-- Services section -->
<section><header><h2>Services</h2><p>We work with you</p></header><div><h3>Design &amp; Concept</h3><h3>Digital Strategy</h3><h3>Content Strategy</h3><h3>UX Design</h3><h3>Web Development</h3><h3>Social Media</h3></div></section>
<!-- Works section -->
<section><header><h2>Works</h2><p>Take a look in our portfolio</p></header><div><article><h3>Interior Design</h3></article><article><h3>Web Development</h3></article><article><h3>Personal Brand</h3></article></div></section>
<!-- About Us section -->
<section><header><h2>About Us</h2><p>Everything about us</p></header><div><h3>Who are we</h3><p>Lorem ipsum</p><h3>Our culture</h3><p>Lorem ipsum</p><h3>How we work</h3><p>Lorem ipsum</p><a href="about.html">Learn more about us</a></div></section>
<!-- Latest news section -->
<section><header><h2>Latest news</h2></header><div><article><h3>Hoc loco tenere se Triarius non potuit.</h3></article><article><h3>Ut alios omittam, hunc appello, quem ille unum secutus est.</h3></article><article><h3>Bestiarum vero nullum iudicium puto.</h3></article></div></section>
<!-- Testimonials section -->
<section><header><h2>Testimonials</h2><p>We are more than a digital company</p></header><div><article><blockquote>I am completely blown away. Thanks to Techium, we've just launched our 5th website! <cite>Yuri Y.</cite></blockquote></article><article><blockquote>Thank you so much for your help. Techium company is awesome! <cite>Dorrie S.</cite></blockquote></article><article><blockquote>I love your system. Definitely worth the investment. I'd be lost without Techium company. <cite>Sven H.</cite></blockquote></article></div></section>
<!-- Contact section -->
<section><header><h2>Contact</h2><p>We like to know new people</p></header><div><p>Lorem ipsum</p><a href="contact.html">Get in touch</a></div></section></main>
<!-- Footer to help with scanning your code -->
<footer><div>Footer</div></footer>'''
write("17-index.html", page("Homepage - Techium", comments))

for name, title in (("about.html", "About"), ("latest_news.html", "Latest news"), ("contact.html", "Contact")):
    write(name, page(f"{title} - Techium", f'''{header}<main><h1>{title}</h1></main>{footer}'''))

write("20-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1></main>{footer}'''))
write("21-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1></main><footer>{social}</footer>'''))
write("22-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1>{sections}</main><footer>{social}</footer>'''))
write("23-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1>{sections}</main><footer>{social}</footer>'''))
write("24-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1>{sections}</main><footer>{social}</footer>'''))
write("25-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1>{sections}</main><footer>{social}{secondary}</footer>'''))
write("27-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1>{sections}</main><footer>{social}{secondary}<hr><p>© 2020 Techium, made with ♥ by students at Holberton School.</p></footer>'''))
write("29-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1>{sections}</main>{footer}'''))
write("31-index.html", page("Homepage - Techium", f'''{header}<main><h1>Homepage</h1>{sections}</main>{footer}'''))

media_sections = '''<section id="works"><header><h2>Works</h2><p>Take a look in our portfolio</p></header><div><article><div><img src="images/pic-work-01.jpg" alt=""></div><h3>Interior Design</h3></article><article><div><img src="images/pic-work-02.jpg" alt=""></div><h3>Web Development</h3></article><article><div><img src="images/pic-work-03.jpg" alt=""></div><h3>Personal Brand</h3></article></div></section>
<section id="about"><header><h2>About Us</h2><p>Everything about us</p></header><div><img src="images/pic-about-us.jpg" alt="" width="460" height="447"><h3>Who are we</h3></div></section>
<section id="latest_news"><header><h2>Latest news</h2></header><div><article><div><img src="images/pic-blog-01.jpg" alt="" width="305" height="205"></div><p>Career</p><h3>Hoc loco tenere se Triarius non potuit.</h3></article><article><div><img src="images/pic-blog-02.jpg" alt="" width="305" height="205"></div><p>Digital Life</p><h3>Ut alios omittam, hunc appello, quem ille unum secutus est.</h3></article><article><div><img src="images/pic-blog-03.jpg" alt="" width="305" height="205"></div><p>Social</p><h3>Bestiarum vero nullum iudicium puto.</h3></article></div></section>
<section id="testimonials"><header><h2>Testimonials</h2><p>We are more than a digital company</p></header><div><article><img src="images/pic-person-01.jpg" alt="Yuri Y. avatar" width="100" height="100"><blockquote>I am completely blown away. Thanks to Techium, we've just launched our 5th website! <cite>Yuri Y.</cite></blockquote></article><article><img src="images/pic-person-02.jpg" alt="Dorrie S. avatar" width="100" height="100"><blockquote>Thank you so much for your help. Techium company is awesome! <cite>Dorrie S.</cite></blockquote></article><article><img src="images/pic-person-03.jpg" alt="Sven H. avatar" width="100" height="100"><blockquote>I love your system. Definitely worth the investment. <cite>Sven H.</cite></blockquote></article></div></section>'''
write("35-index.html", page("Homepage - Techium", f'''<header><div><img src="logo-black.png" alt="Techium logo" width="160" height="40"></div>{nav}</header><main><h1>Homepage</h1>{sections}</main>{footer}'''))
write("36-index.html", page("Homepage - Techium", f'''<header><div><img src="logo-black.png" alt="Techium logo" width="160" height="40"></div>{nav}</header><main><h1>Homepage</h1><section><header><h2>We help you build your brand!</h2></header><div><a href="#">Get started</a></div></section><section id="services"><header><h2>Services</h2><p>We work with you</p></header><div><h3>Design &amp; Concept</h3><h3>Digital Strategy</h3><h3>Content Strategy</h3><h3>UX Design</h3><h3>Web Development</h3><h3>Social Media</h3></div></section>{media_sections}<section id="contact"><header><h2>Contact</h2><p>We like to know new people</p></header><div><p>Lorem ipsum</p><a href="contact.html">Get in touch</a></div></section></main>{footer}'''))

write("38-styleguide.html", page("Styleguide - Techium", '''<header></header><main><section><header><h2>Video</h2></header><video controls loop poster="https://intranet-projects-files.s3.amazonaws.com/webstack/thumbnail.jpg"><source src="https://intranet-projects-files.s3.amazonaws.com/webstack/BigBuckBunny.mp4" type="video/mp4">Sorry, your browser doesn't support HTML5 video</video></section></main><footer></footer>'''))
write("39-styleguide.html", page("Styleguide - Techium", '''<header></header><main><section><header><h2>Video</h2></header><video controls loop poster="https://intranet-projects-files.s3.amazonaws.com/webstack/thumbnail.jpg"><source src="https://intranet-projects-files.s3.amazonaws.com/webstack/BigBuckBunny.mp4" type="video/mp4">Sorry, your browser doesn't support HTML5 video</video></section><section><header><h2>Audio</h2></header><audio controls><source src="https://intranet-projects-files.s3.amazonaws.com/webstack/TroubleChapter8_64kb.mp3" type="audio/mpeg">Sorry, your browser doesn't support audio element</audio></section></main><footer></footer>'''))
write("styleguide.html", page("Styleguide - Techium", '''<header></header><main><section><header><h2>Audio</h2></header><audio controls><source src="https://intranet-projects-files.s3.amazonaws.com/webstack/TroubleChapter8_64kb.mp3" type="audio/mpeg">Sorry, your browser doesn't support audio element</audio></section><section><header><h2>Iframe</h2></header><div><iframe title="Holberton School" width="350" height="200" src="https://www.youtube.com/embed/41N6bKO-NVI">Holberton Sally</iframe></div></section></main><footer></footer>'''))

print("Repaired assignment HTML files")

# Rebuild the styleguide copy-forward chain with every earlier section retained.
headings = '<section><header><h2>Headings</h2></header><h1>Heading level 1</h1><h2>Heading level 2</h2><h3>Heading level 3</h3><h4>Heading level 4</h4><h5>Heading level 5</h5><h6>Heading level 6</h6></section>'
paragraphs = '<section><header><h2>Paragraph</h2></header><h2>Heading with a subtitle</h2><p>This is my subtitle</p><p>Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet. Volutpat eu sed ante lacinia sapien lorem accumsan varius montes viverra nibh in adipiscing blandit tempus accumsan.</p></section>'
lists = '<section><header><h2>Lists</h2></header><div><h3>Unordered</h3><ul><li>Dolor pulvinar etiam magna etiam.</li><li>Sagittis adipiscing lorem eleifend.</li><li>Felis enim feugiat dolore viverra.</li></ul><h3>Ordered</h3><ol><li>Dolor pulvinar etiam magna etiam.</li><li>Sagittis adipiscing lorem eleifend.</li><li>Felis enim feugiat dolore viverra.</li></ol><h3>Definition</h3><dl><dt>Definition List title</dt><dd>Definition text.</dd><dt>Startup</dt><dd>A startup company or startup is a company or temporary organization designed to search for a repeatable and scalable business model.</dd><dt>Water</dt><dd>A colorless, transparent, odorless liquid that forms the seas, lakes, rivers, and rain and is the basis of the fluids of living organisms.</dd></dl></div></section>'
horizontal_rule = '<section><header><h2>Horizontal rule</h2></header><div><hr></div></section>'
blockquotes = '<section><header><h2>Blockquotes</h2></header><div><h3>Inline quote</h3><q>Stay hungry. Stay foolish.</q></div><div><h3>Blockquote</h3><blockquote>I will be the leader of a company that ends up being worth billions of dollars, because I got the answers. I understand culture. I am the nucleus. I think that’s a responsibility that I have, to push possibilities, to show people, this is the level that things could be at.<cite>Kanye West, Musician</cite></blockquote></div></section>'
typography = '<section><header><h2>Typography</h2></header><div><address>320 Stewart Avenue, Unit 12<br>New York City NY 10001</address></div><div><pre><code>&lt;h2&gt;My title&lt;/h2&gt;\n    &lt;p&gt;Proin lacus turpis, feugiat sit amet sollicitudin non, volutpat in libero. Aenean hendrerit ultrices nulla ac lobortis. Vestibulum consectetur nibh vel ante rhoncus faucibus.&lt;/p&gt;\n&lt;/code&gt;</pre></div><div><p>Curabitur sit amet turpis cursus massa mollis <mark>highlighted</mark>. Duis finibus leo massa, eget dapibus erat finibus sed. Aenean condimentum sapien magna, eleifend <mark>highlighted</mark> mi consequat ut. Cras nec quam sed sapien ultricies <mark>highlighted</mark> ut sed metus.</p></div></section>'
table = '<section><header><h2>Table</h2></header><table><thead><tr><th scope="col">Title</th><th scope="col">Director</th><th scope="col">Release Date</th></tr></thead><tbody><tr><th scope="row">The Shawshank Redemption</th><td>Frank Darabont</td><td>1994</td></tr><tr><th scope="row">The Godfather</th><td>Francis Ford Coppola</td><td>1972</td></tr><tr><th scope="row">The Dark Knight</th><td>Christopher Nolan</td><td>2008</td></tr></tbody></table></section>'
details = '<section><header><h2>Details</h2></header><div><h3>Default</h3><details><summary>Show/Hide me</summary>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</details></div><div><h3>Open</h3><details open><summary>Always open</summary>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</details></div></section>'
video = '<section><header><h2>Video</h2></header><video controls loop poster="https://intranet-projects-files.s3.amazonaws.com/webstack/thumbnail.jpg"><source src="https://intranet-projects-files.s3.amazonaws.com/webstack/BigBuckBunny.mp4" type="video/mp4">Sorry, your browser doesn\'t support HTML5 video</video></section>'
audio = '<section><header><h2>Audio</h2></header><audio controls><source src="https://intranet-projects-files.s3.amazonaws.com/webstack/TroubleChapter8_64kb.mp3" type="audio/mpeg">Sorry, your browser doesn\'t support audio element</audio></section>'
iframe = '<section><header><h2>Iframe</h2></header><div><iframe title="Holberton School" width="350" height="200" src="https://www.youtube.com/embed/41N6bKO-NVI">Holberton Sally</iframe></div></section>'

write("11-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}</main><footer></footer>'))
write("13-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}</main><footer></footer>'))
write("26-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}</main><footer></footer>'))
write("28-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}<!-- Horizontal rule -->{horizontal_rule}</main><footer></footer>'))
write("30-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}{horizontal_rule}<!-- Blockquotes -->{blockquotes}</main><footer></footer>'))
write("32-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}{horizontal_rule}{blockquotes}<!-- Typography -->{typography}</main><footer></footer>'))
write("33-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}{horizontal_rule}{blockquotes}{typography}<!-- Table -->{table}</main><footer></footer>'))
write("34-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}{horizontal_rule}{blockquotes}{typography}{table}<!-- Details -->{details}</main><footer></footer>'))
write("38-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}{horizontal_rule}{blockquotes}{typography}{table}{details}<!-- Video -->{video}</main><footer></footer>'))
write("39-styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}{horizontal_rule}{blockquotes}{typography}{table}{details}{video}<!-- Audio -->{audio}</main><footer></footer>'))
write("styleguide.html", page("Styleguide - Techium", f'<header></header><main>{headings}{paragraphs}{lists}{horizontal_rule}{blockquotes}{typography}{table}{details}{video}{audio}<!-- Iframe -->{iframe}</main><footer></footer>'))

# The navigation and page-copy tasks must preserve the complete homepage built
# by task 17; only the requested link or footer change is added at each step.
home_header = '<header><div><a href="/"><span>Techium</span></a></div>' + nav + '</header>'
home_main = '<main><h1>Homepage</h1>' + sections + '</main>'
simple_footer = '<footer><div>Footer</div></footer>'
write("14-index.html", page("Homepage - Techium", '<header><div><span>Techium</span></div><nav></nav></header>' + home_main + simple_footer))
write("18-index.html", page("Homepage - Techium", home_header + home_main + simple_footer))
for name, title, heading in (("about.html", "About", "About"), ("latest_news.html", "Latest news", "Latest news"), ("contact.html", "Contact", "Contact")):
  write(name, page(f"{title} - Techium", home_header + '<main><h1>' + heading + '</h1>' + sections + '</main>' + simple_footer))
write("20-index.html", page("Homepage - Techium", home_header + home_main + simple_footer))
write("21-index.html", page("Homepage - Techium", home_header + home_main + '<footer>' + social + '</footer>'))
write("22-index.html", page("Homepage - Techium", home_header + home_main + '<footer>' + social + '</footer>'))
write("23-index.html", page("Homepage - Techium", home_header + home_main + '<footer>' + social + '</footer>'))
write("24-index.html", page("Homepage - Techium", home_header + home_main + '<footer>' + social + '</footer>'))
write("25-index.html", page("Homepage - Techium", home_header + home_main + '<footer>' + social + secondary + '</footer>'))

# Rebuild the early progression exactly: each task copies the preceding page and
# adds only the requested semantic element.
early_sections = '''<section>Hero section</section>
<section>Services section</section>
<section>Works section</section>
<section>About section</section>
<section>Latest news section</section>
<section>Testimonials section</section>
<section>Contact section</section>'''
write("5-index.html", page("Homepage - Techium", '<header>Header</header><main>' + early_sections + '</main><footer>Footer</footer>'))
write("6-index.html", page("Homepage - Techium", '<header>Header</header><main><section>Hero section</section><section>Services section</section><section>Works section<article>Work #1</article><article>Work #2</article><article>Work #3</article></section><section>About section</section><section>Latest news section<article>Article #1</article><article>Article #2</article><article>Article #3</article></section><section>Testimonials section<article>Testimonial #1</article><article>Testimonial #2</article><article>Testimonial #3</article></section><section>Contact section</section></main><footer>Footer</footer>'))
semantic_sections = '<section><h2>Hero section</h2></section><section><h2>Services section</h2></section><section><h2>Works section</h2><article>Work #1</article><article>Work #2</article><article>Work #3</article></section><section><h2>About section</h2></section><section><h2>Latest news section</h2><article>Article #1</article><article>Article #2</article><article>Article #3</article></section><section><h2>Testimonials section</h2><article>Testimonial #1</article><article>Testimonial #2</article><article>Testimonial #3</article></section><section><h2>Contact section</h2></section>'
write("7-index.html", page("Homepage - Techium", '<header><nav></nav></header><main>' + '<section>Hero section</section><section>Services section</section><section>Works section<article>Work #1</article><article>Work #2</article><article>Work #3</article></section><section>About section</section><section>Latest news section<article>Article #1</article><article>Article #2</article><article>Article #3</article></section><section>Testimonials section<article>Testimonial #1</article><article>Testimonial #2</article><article>Testimonial #3</article></section><section>Contact section</section>' + '</main><footer>Footer</footer>'))
write("8-index.html", page("Homepage - Techium", '<header><nav></nav></header><main><h1>Homepage</h1>' + '<section>Hero section</section><section>Services section</section><section>Works section<article>Work #1</article><article>Work #2</article><article>Work #3</article></section><section>About section</section><section>Latest news section<article>Article #1</article><article>Article #2</article><article>Article #3</article></section><section>Testimonials section<article>Testimonial #1</article><article>Testimonial #2</article><article>Testimonial #3</article></section><section>Contact section</section>' + '</main><footer>Footer</footer>'))
headings_sections = '<section><h2>We help you build your brand!</h2></section><section><h2>Services</h2></section><section><h2>Works</h2></section><section><h2>About Us</h2></section><section><h2>Latest news</h2></section><section><h2>Testimonials</h2></section><section><h2>Contact</h2></section>'
write("9-index.html", page("Homepage - Techium", '<header><nav></nav></header><main><h1>Homepage</h1>' + headings_sections + '</main><footer>Footer</footer>'))
level_three = '<section><h2>We help you build your brand!</h2></section><section><h2>Services</h2><h3>Design &amp; Concept</h3><h3>Digital Strategy</h3><h3>Content Strategy</h3><h3>UX Design</h3><h3>Web Development</h3><h3>Social Media</h3></section><section><h2>Works</h2><article><h3>Interior Design</h3></article><article><h3>Web Development</h3></article><article><h3>Personal Brand</h3></article></section><section><h2>About Us</h2><h3>Who are we</h3><h3>Our culture</h3><h3>How we work</h3></section><section><h2>Latest news</h2><article><h3>Hoc loco tenere se Triarius non potuit.</h3></article><article><h3>Ut alios omittam, hunc appello, quem ille unum secutus est.</h3></article><article><h3>Bestiarum vero nullum iudicium puto.</h3></article></section><section><h2>Testimonials</h2></section><section><h2>Contact</h2></section>'
write("10-index.html", page("Homepage - Techium", '<header><nav></nav></header><main><h1>Homepage</h1>' + level_three + '</main><footer>Footer</footer>'))

# Task 12 content is the source for the div and section-wrapper exercises.
about_content = '<h3>Who are we</h3><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p><h3>Our culture</h3><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p><h3>How we work</h3><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p>'
news_content = '<article><p>Career</p><h3>Hoc loco tenere se Triarius non potuit.</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Id Sextilius factum negabat. Quo tandem modo? At eum nihili facit; Quae contraria sunt his, malane?</p></article><article><p>Digital Life</p><h3>Ut alios omittam, hunc appello, quem ille unum secutus est.</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Tum mihi Piso: Quid ergo? Tum ille: Ain tandem? Non autem hoc: igitur ne illud quidem. Sed quod proximum fuit non vidit. Nos commodius agimus. An nisi populari fama?</p></article><article><p>Social</p><h3>Bestiarum vero nullum iudicium puto.</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Non igitur bene. Quid enim est a Chrysippo praetermissum in Stoicis? Pugnant Stoici cum Peripateticis. Prioris generis est docilitas, memoria; Apparet statim, quae sint officia, quae actiones.</p></article>'
task12 = '<header><nav></nav></header><main><h1>Homepage</h1><section><h2>We help you build your brand!</h2></section><section><h2>Services</h2><p>We work with you</p><h3>Design &amp; Concept</h3><h3>Digital Strategy</h3><h3>Content Strategy</h3><h3>UX Design</h3><h3>Web Development</h3><h3>Social Media</h3></section><section><h2>Works</h2><p>Take a look in our portfolio</p><article><h3>Interior Design</h3></article><article><h3>Web Development</h3></article><article><h3>Personal Brand</h3></article></section><section><h2>About Us</h2><p>Everything about us</p>' + about_content + '</section><section><h2>Latest news</h2>' + news_content + '</section><section><h2>Testimonials</h2><p>We are more than a digital company</p></section><section><h2>Contact</h2><p>We like to know new people</p><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Id Sextilius factum negabat. Quo tandem modo? At eum nihili facit; Quae contraria sunt his, malane?</p></section></main><footer>Footer</footer>'
write("12-index.html", page("Homepage - Techium", task12))
write("14-index.html", page("Homepage - Techium", task12.replace('<header><nav>', '<header><span>Techium</span><nav>')))
section_divs = '<section><div><h2>We help you build your brand!</h2></div></section><section><div><h2>Services</h2><p>We work with you</p></div><div><h3>Design &amp; Concept</h3><h3>Digital Strategy</h3><h3>Content Strategy</h3><h3>UX Design</h3><h3>Web Development</h3><h3>Social Media</h3></div></section><section><div><h2>Works</h2><p>Take a look in our portfolio</p></div><div><article><h3>Interior Design</h3></article><article><h3>Web Development</h3></article><article><h3>Personal Brand</h3></article></div></section><section><div><h2>About Us</h2><p>Everything about us</p></div><div>' + about_content + '</div></section><section><div><h2>Latest news</h2></div><div>' + news_content + '</div></section><section><div><h2>Testimonials</h2><p>We are more than a digital company</p></div><div><article>Testimonial #1</article><article>Testimonial #2</article><article>Testimonial #3</article></div></section><section><div><h2>Contact</h2><p>We like to know new people</p></div><div><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Id Sextilius factum negabat. Quo tandem modo? At eum nihili facit; Quae contraria sunt his, malane?</p></div></section>'
write("15-index.html", page("Homepage - Techium", '<header><div><span>Techium</span><nav></nav></div></header><main><h1>Homepage</h1>' + section_divs + '</main><footer><div>Footer</div></footer>'))
structured = section_divs.replace('<section><div><h2>Services</h2><p>We work with you</p></div><div>', '<section><div><header><h2>Services</h2><p>We work with you</p></header></div><div>').replace('<section><div><h2>Works</h2><p>Take a look in our portfolio</p></div><div>', '<section><div><header><h2>Works</h2><p>Take a look in our portfolio</p></header></div><div>').replace('<section><div><h2>About Us</h2><p>Everything about us</p></div><div>', '<section><div><header><h2>About Us</h2><p>Everything about us</p></header></div><div>').replace('<section><div><h2>Latest news</h2></div><div>', '<section><div><header><h2>Latest news</h2></header></div><div>').replace('<section><div><h2>Testimonials</h2><p>We are more than a digital company</p></div><div>', '<section><div><header><h2>Testimonials</h2><p>We are more than a digital company</p></header></div><div>').replace('<section><div><h2>Contact</h2><p>We like to know new people</p></div><div>', '<section><div><header><h2>Contact</h2><p>We like to know new people</p></header></div><div>')
write("16-index.html", page("Homepage - Techium", '<header><div><span>Techium</span><nav></nav></div></header><main><h1>Homepage</h1>' + structured + '</main><footer><div>Footer</div></footer>'))

commented_structured = structured.replace('<section>', '<!-- Hero section -->\n<section>', 1)
for label, marker in (("Services section", '<section><div><header><h2>Services'), ("Works section", '<section><div><header><h2>Works'), ("About Us section", '<section><div><header><h2>About Us'), ("Latest news section", '<section><div><header><h2>Latest news'), ("Testimonials section", '<section><div><header><h2>Testimonials'), ("Contact section", '<section><div><header><h2>Contact')):
  commented_structured = commented_structured.replace(marker, '<!-- ' + label + ' -->\n' + marker, 1)
commented_body = '<!-- Header to help with scanning your code -->\n<header><div><span>Techium</span><nav></nav></div></header>\n<!-- Main to help with scanning your code -->\n<main><h1>Homepage</h1>\n' + commented_structured + '</main>\n<!-- Footer to help with scanning your code -->\n<footer><div>Footer</div></footer>'
write("17-index.html", page("Homepage - Techium", commented_body))
write("18-index.html", page("Homepage - Techium", commented_body.replace('<span>Techium</span><nav></nav>', '<a href="/"><span>Techium</span></a><nav></nav>')))
write("20-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main>' + simple_footer))
write("21-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main><footer>' + social + '</footer>'))
write("22-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main><footer>' + social + '</footer>'))
write("23-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main><footer>' + social + '</footer>'))
write("24-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main><footer>' + social + '</footer>'))
write("25-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main><footer>' + social + secondary + '</footer>'))

# Final homepage chain: keep task 31 free of the task-35 logo, place the task-35
# footer image directly before the address, and copy the complete media page to index.html.
footer27 = '<footer>' + social + '<hr><p>© 2020 Techium, made with ♥ by students at Holberton School.</p>' + secondary + '</footer>'
write("27-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main>' + footer27))
write("29-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main>' + footer27))
footer31 = '<footer><address>234 Washington Street<br>Urbana, Illinois</address>' + social + '<hr><p>© 2020 Techium, made with ♥ by students at Holberton School.</p>' + secondary + '</footer>'
write("31-index.html", page("Homepage - Techium", home_header + '<main><h1>Homepage</h1>' + sections + '</main>' + footer31))
footer35 = '<footer><img src="logo-black.png" alt="Techium logo" width="160" height="40"><address>234 Washington Street<br>Urbana, Illinois</address>' + social + '<hr><p>© 2020 Techium, made with ♥ by students at Holberton School.</p>' + secondary + '</footer>'
write("35-index.html", page("Homepage - Techium", '<header><div><img src="logo-black.png" alt="Techium logo" width="160" height="40"></div>' + nav + '</header><main><h1>Homepage</h1>' + sections + '</main>' + footer35))
write("36-index.html", page("Homepage - Techium", '<header><div><img src="logo-black.png" alt="Techium logo" width="160" height="40"></div>' + nav + '</header><main><h1>Homepage</h1><section><header><h2>We help you build your brand!</h2></header><div><a href="#">Get started</a></div></section><section id="services"><header><h2>Services</h2><p>We work with you</p></header><div><h3>Design &amp; Concept</h3><h3>Digital Strategy</h3><h3>Content Strategy</h3><h3>UX Design</h3><h3>Web Development</h3><h3>Social Media</h3></div></section>' + media_sections + '<section id="contact"><header><h2>Contact</h2><p>We like to know new people</p></header><div><p>Lorem ipsum</p><a href="contact.html">Get in touch</a></div></section></main>' + footer35))
svg_social = '''<footer><ul><li><a href="https://www.facebook.com/HolbertonSchool/"><svg width="25" height="25" viewBox="0 0 24 24"><path d="M13.5 21v-8h2.5l.5-3h-3V7.5c0-.9.3-1.5 1.7-1.5H16V3.1c-.3 0-1.3-.1-2.4-.1C11.1 3 9.5 4.4 9.5 7v3H7v3h2.5v8h4z"></path></svg></a></li><li><a href="https://twitter.com/holbertonschool"><svg width="25" height="25" viewBox="0 0 24 24"><path d="M22 5.9c-.7.3-1.4.5-2.2.6.8-.5 1.4-1.2 1.7-2.1-.8.5-1.7.8-2.6 1A4.1 4.1 0 0 0 12 8.1c0 .3 0 .6.1 1A11.6 11.6 0 0 1 3.4 5.1a4.2 4.2 0 0 0 1.3 5.6c-.6 0-1.2-.2-1.7-.5v.1c0 2 1.4 3.7 3.3 4.1-.3.1-.7.1-1 .1-.3 0-.5 0-.8-.1.5 1.6 2 2.8 3.8 2.8A8.3 8.3 0 0 1 2 18.5a11.7 11.7 0 0 0 6.3 1.8c7.6 0 11.8-6.2 11.8-11.6v-.5c.8-.6 1.5-1.3 2.1-2.1z"></path></svg></a></li><li><a href="https://www.instagram.com/holbertonschool/"><svg width="25" height="25" viewBox="0 0 24 24"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7zm5 3.8A4.2 4.2 0 1 1 7.8 12 4.2 4.2 0 0 1 12 7.8zm0 2A2.2 2.2 0 1 0 14.2 12 2.2 2.2 0 0 0 12 9.8z"></path></svg></a></li></ul></footer>'''
svg_social_div = svg_social.replace('<footer>', '<div>').replace('</footer>', '</div>')
write("index.html", page("Homepage - Techium", '<header><div><img src="logo-black.png" alt="Techium logo" width="160" height="40"></div>' + nav + '</header><main><h1>Homepage</h1><section><h2>We help you build your brand!</h2></section><section id="services"><h2>Services</h2><p>We work with you</p><h3>Design &amp; Concept</h3><h3>Digital Strategy</h3><h3>Content Strategy</h3><h3>UX Design</h3><h3>Web Development</h3><h3>Social Media</h3></section>' + media_sections + '<section id="contact"><h2>Contact</h2><p>We like to know new people</p><a href="contact.html">Get in touch</a></section></main><footer><img src="logo-black.png" alt="Techium logo" width="160" height="40"><address>234 Washington Street<br>Urbana, Illinois</address>' + svg_social_div + secondary + '<hr><p>© 2020 Techium, made with ♥ by students at Holberton School.</p></footer>'))

# Task 19 is deliberately only a title change from task 18.
linked_body = commented_body.replace('<span>Techium</span><nav></nav>', '<a href="/"><span>Techium</span></a><nav></nav>')
write("about.html", page("About - Techium", linked_body))
write("latest_news.html", page("Latest news - Techium", linked_body))
write("contact.html", page("Contact - Techium", linked_body))

media_for_36 = media_sections.replace('</h3></article><article><div><img src="images/pic-blog-02.jpg"', '</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p><small>By Kelly D.</small></article><article><div><img src="images/pic-blog-02.jpg"', 1).replace('</h3></article><article><div><img src="images/pic-blog-03.jpg"', '</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p><small>By William A.</small></article><article><div><img src="images/pic-blog-03.jpg"', 1).replace('</h3></article></div></section>\n<section id="testimonials"', '</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p><small>By Frances J.</small></article></div></section>\n<section id="testimonials"', 1)
for name in ("36-index.html", "index.html"):
  generated = (ROOT / name).read_text(encoding="utf-8")
  generated = generated.replace(media_sections, media_for_36)
  generated = generated.replace('<h3>Hoc loco tenere se Triarius non potuit.</h3>', '<h3>Hoc loco tenere se Triarius non potuit.</h3><small>By Kelly D.</small>')
  generated = generated.replace('<h3>Ut alios omittam, hunc appello, quem ille unum secutus est.</h3>', '<h3>Ut alios omittam, hunc appello, quem ille unum secutus est.</h3><small>By William A.</small>')
  generated = generated.replace('<h3>Bestiarum vero nullum iudicium puto.</h3>', '<h3>Bestiarum vero nullum iudicium puto.</h3><small>By Frances J.</small>')
  (ROOT / name).write_text(generated, encoding="utf-8")