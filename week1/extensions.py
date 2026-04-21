
def helper(x):
    
    return x.split(".")[-1].strip().lower()

def main():
    x=input("File name: ")

    filename=helper(x)
    match filename:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()
