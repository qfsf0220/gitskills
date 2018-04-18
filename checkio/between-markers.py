def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    a,b= text.find(begin),text.find(end)
    print(a,b)
    if a>=0 and b>=0:
        print(text[a+len(begin):b])
        return(text[a+len(begin):b])
    elif a>=0 and b<=0:
        print(text[a+len(begin):])
        return(text[a+len(begin):])
    elif a<=0 and b>=0:
        print(text[:b])
        return(text[:b])
    else:
        print(text)
        return(text)
#
# between_markers('No [b]hi', '[b]', '[/b]')   # hi
#
# between_markers('No[/b] hi', '[b]', '[/b]') # No
between_markers('What is >apple<', '>', '<')
between_markers("Never send a human to do a machine's job.", "Never", "do")

# if __name__ == '__main__':
#     print('Example:')
#     print(between_markers('What is >apple<', '>', '<'))
#
#     # These "asserts" are used for self-checking and not for testing
#     assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
#     assert between_markers("<head><title>My new site</title></head>",
#                            "<title>", "</title>") == "My new site", "HTML"
#     assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
#     assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
#     assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
#     assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
#     print('Wow, you are doing pretty good. Time to check it!')