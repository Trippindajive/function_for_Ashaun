# variables and lists at the very core
content = []
timContent = []
author = ["A'shaun", "Brandt"]
title = "This Is Blog "
subtitle = ["One", "Two"]
start_of_blog = ('\n~' + '\n')

# variables concatenting the core variables (Ashaun or Brandt)
title_of_blog_A = (author[0] + '\n\t' + title + subtitle[0])
title_of_blog_B = (author[1] + '\n\t' + title + subtitle[1])

# finished products
portion_of_blog = (start_of_blog)
complete_title_A = (title_of_blog_A + portion_of_blog)
complete_title_B = (title_of_blog_B + start_of_blog)

# lines below test program
print (complete_title_A)
print (timContent.append(complete_title_A))










