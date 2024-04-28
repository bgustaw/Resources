import subprocess

project_base_filepath = r"C:\Users"
folders = ("scripts", "stylesheets")

for folder in folders:
    subprocess.run(["python", "css_html_js_minify/css-html-js-minify.py", project_base_filepath+folder])
