from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes[0].text_type != TextType.TEXT:
        return old_nodes
    if old_nodes[0].text.count(delimiter) != 2:
        raise Exception("Invalid Markdown Syntax")
    new_nodes = old_nodes[0].text.split(delimiter)
    group = []
    for i in range(len(new_nodes)):
        if i != 1:
            group.append(TextNode(new_nodes[i], TextType.TEXT))
        elif delimiter == "`":
            group.append(TextNode(new_nodes[i], TextType.CODE))
        elif delimiter == "**":
            group.append(TextNode(new_nodes[i], TextType.BOLD))
        elif delimiter == "_":
            group.append(TextNode(new_nodes[i], TextType.ITALIC))
    return group
