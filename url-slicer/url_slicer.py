
url = input("Enter your URL: ")

protocol = url[:url.index(":")]
domain = url[url.index("//") +2:url.index(".")]
extension = url[url.index("."):]

print(f"Your protocol is {protocol} and your domain is {domain} and the estension is {extension}")


