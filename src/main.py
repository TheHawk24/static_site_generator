from copydir import copy_to
from page_generator import generate_page, generate_pages_recursive

def generator():
    copy_to('./static/', './public/')
    generate_pages_recursive('./content/', 'template.html', './public/')

def main():

    generator()

if __name__ == "__main__":
    main()
