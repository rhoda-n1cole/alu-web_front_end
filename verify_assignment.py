from pathlib import Path

root = Path(r"C:\Users\niecy\alu-web_front_end\html_advanced")

required_files = {
    "0-index.html",
    "1-index.html",
    "2-index.html",
    "3-index.html",
    "4-index.html",
    "5-index.html",
    "6-index.html",
    "7-index.html",
    "8-index.html",
    "9-index.html",
    "10-index.html",
    "11-styleguide.html",
    "12-index.html",
    "13-styleguide.html",
    "14-index.html",
    "15-index.html",
    "16-index.html",
    "17-index.html",
    "18-index.html",
    "19-index.html",
    "20-index.html",
    "21-index.html",
    "22-index.html",
    "23-index.html",
    "24-index.html",
    "25-index.html",
    "26-styleguide.html",
    "27-index.html",
    "28-styleguide.html",
    "29-index.html",
    "30-styleguide.html",
    "31-index.html",
    "32-styleguide.html",
    "33-styleguide.html",
    "34-styleguide.html",
    "35-index.html",
    "36-index.html",
    "38-styleguide.html",
    "39-styleguide.html",
    "about.html",
    "article.html",
    "contact.html",
    "index.html",
    "latest_news.html",
    "styleguide.html",
}

missing = sorted(required_files - {p.name for p in root.iterdir() if p.is_file()})
if missing:
    raise AssertionError(f"Missing required files: {missing}")

checks = {
    "0-index.html": ["<!DOCTYPE html>", "<html lang=\"en\" dir=\"ltr\">"],
    "1-index.html": ["<head></head>", "<body></body>"],
    "2-index.html": ["meta charset=\"utf-8\"", "name=\"viewport\"", "<title>Homepage - Techium</title>", "Techium is a digital agency", "./favicon.ico", "./favicon.png"],
    "3-index.html": ["<header>Header</header>", "<main>Main content</main>", "<footer>Footer</footer>"],
    "article.html": ["<title>Article - Techium</title>", "<aside>Aside</aside>"],
    "5-index.html": ["Hero section", "Services section", "Works section", "About section", "Latest news section", "Testimonials section", "Contact section"],
    "6-index.html": ["Work #1", "Work #2", "Work #3", "Article #1", "Article #2", "Article #3", "Testimonial #1", "Testimonial #2", "Testimonial #3"],
    "7-index.html": ["<nav></nav>"],
    "8-index.html": ["<h1>Homepage</h1>"],
    "9-index.html": ["We help you build your brand!", "Services", "Works", "About Us", "Latest news", "Testimonials", "Contact"],
    "10-index.html": ["Design &amp; Concept", "Digital Strategy", "Content Strategy", "UX Design", "Web Development", "Social Media", "Interior Design", "Personal Brand", "Who are we", "Our culture", "How we work"],
    "11-styleguide.html": ["Heading level 1", "Heading level 2", "Heading level 3", "Heading level 4", "Heading level 5", "Heading level 6"],
    "12-index.html": ["We work with you", "Take a look in our portfolio", "Everything about us", "We are more than a digital company", "We like to know new people", "Career", "Digital Life", "Social"],
    "13-styleguide.html": ["Heading with a subtitle", "This is my subtitle", "Nunc lacinia ante nunc ac lobortis."],
    "14-index.html": ["<span>Techium</span>"],
    "15-index.html": ["<div>", "<header>", "<footer>"],
    "16-index.html": ["<header>", "<div>", "<h2>Services</h2>", "<h2>Works</h2>", "<h2>About Us</h2>", "<h2>Latest news</h2>", "<h2>Testimonials</h2>", "<h2>Contact</h2>"],
    "17-index.html": ["Header to help with scanning your code", "Main to help with scanning your code", "Footer to help with scanning your code", "Hero section", "Services section", "Works section", "About Us section", "Latest news section", "Testimonials section", "Contact section"],
    "18-index.html": ["<a href=\"/\">Techium</a>"],
    "about.html": ["<title>About - Techium</title>"],
    "latest_news.html": ["<title>Latest news - Techium</title>"],
    "contact.html": ["<title>Contact - Techium</title>"],
    "20-index.html": ["Home</a>", "Services</a>", "Works</a>", "About</a>", "Latest news</a>", "Testimonials</a>", "Contact</a>"],
    "21-index.html": ["Facebook", "Twitter", "Instagram"],
    "22-index.html": ["Get started", "Learn more about us", "Get in touch"],
    "23-index.html": ["<a href=\"#\">Design &amp; Concept</a>", "<a href=\"#\">Digital Strategy</a>", "<a href=\"#\">Content Strategy</a>", "<a href=\"#\">UX Design</a>", "<a href=\"#\">Web Development</a>", "<a href=\"#\">Social Media</a>"],
    "24-index.html": ["<ul>", "<li><a href=\"/\">Home</a></li>", "<li><a href=\"https://www.facebook.com/HolbertonSchool/\">Facebook</a></li>"],
    "25-index.html": ["Terms of Use", "Privacy Policy", "Cookie Policy"],
    "26-styleguide.html": ["Lists", "Unordered", "Ordered", "Definition", "Definition List title", "Startup", "Water"],
    "27-index.html": ["<hr>", "© 2020 Techium", "made with ♥ by students at Holberton School"],
    "28-styleguide.html": ["Horizontal rule"],
    "29-index.html": ["I am completely blown away. Thanks to Techium, we've just launched our 5th website!", "Yuri Y.", "Thank you so much for your help. Techium company is awesome!", "Dorrie S.", "I love your system. Definitely worth the investment.", "Sven H."],
    "30-styleguide.html": ["Stay hungry. Stay foolish.", "Kanye West, Musician"],
    "31-index.html": ["234 Washington Street", "Urbana, Illinois", "By Kelly D.", "By William A.", "By Frances J."],
    "32-styleguide.html": ["Typography", "320 Stewart Avenue, Unit 12", "<pre>", "<mark>highlighted</mark>"],
    "33-styleguide.html": ["<table>", "scope=\"col\"", "scope=\"row\""],
    "34-styleguide.html": ["<details>", "Show/Hide me", "Always open"],
    "35-index.html": ["logo-black.png", "Techium logo", "width=\"160\"", "height=\"40\""],
    "36-index.html": ["images/pic-work-01.jpg", "images/pic-work-02.jpg", "images/pic-work-03.jpg", "images/pic-about-us.jpg", "images/pic-blog-01.jpg", "images/pic-blog-02.jpg", "images/pic-blog-03.jpg", "images/pic-person-01.jpg", "images/pic-person-02.jpg", "images/pic-person-03.jpg"],
    "38-styleguide.html": ["<video", "BigBuckBunny.mp4", "thumbnail.jpg", "Sorry, your browser doesn't support HTML5 video"],
    "39-styleguide.html": ["<audio", "TroubleChapter8_64kb.mp3", "Sorry, your browser doesn't support audio element"],
    "styleguide.html": ["<iframe title=\"Holberton School\"", "https://www.youtube.com/embed/41N6bKO-NVI", "Holberton Sally"],
    "index.html": ["<svg width=\"25\" height=\"25\"", "https://www.facebook.com/HolbertonSchool/", "https://twitter.com/holbertonschool", "https://www.instagram.com/holbertonschool/"],
}

failed = []
for file_name, needles in checks.items():
    text = (root / file_name).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            failed.append(f"{file_name}: missing -> {needle}")

if failed:
    raise AssertionError("\n".join(failed))

print(f"VALIDATION_OK: {len(checks)} files checked; all required strings found.")
