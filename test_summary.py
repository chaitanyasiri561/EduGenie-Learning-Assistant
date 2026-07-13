from modules.summary import summarize_text

if __name__ == "__main__":
    text = (
        "The Industrial Revolution, which began in the late 18th century, "
        "marked a major turning point in history. It shifted economies from "
        "agriculture and handcraft to industry and machine manufacturing, "
        "starting in Britain and spreading across the world."
    )
    print(summarize_text(text))
    
