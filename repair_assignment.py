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