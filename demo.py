import requests
import xml.etree.ElementTree


# wolformAlphaURL = "http://api.wolframalpha.com/v2/query?appid=Q7K5HX-2Y24EKLAQW&input=5%20%2B%204%20%3F&format=image%2Cplaintext"
#
# import pdb; pdb.set_trace()
# r = requests.get(wolformAlphaURL)
# e = xml.etree.ElementTree.fromstring(r.text)
#
# for f in e:
#     print f


def get_solution_from_wolfarmAlpha(question):
    url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": question,
        "appid": "Q7K5HX-2Y24EKLAQW",
        "format": 'image,plaintext'}
    r = requests.get(url, params=params)
    import pdb
    pdb.set_trace()
    root = xml.etree.ElementTree.fromstring(r.text)
    response = []
    count = 0
    for f in root:
        if count == 0:
            count = count + 1
            continue
        temp = {}
        temp["title"] = f.attrib['title']
        temp["img"] = f[0][0].attrib['src']
        response.append(temp)
        generate_carasol_items(question , temp["img"] , temp["title"] , False)

    send_carasol_items(
        sender,
        [
            generate_carasol_items(
                "Solution Explained",
                temp["img"]),
            generate_carasol_items(
                "Solution Exaplined",
                "http://www.mycompasstest.com/wp-content/uploads/2011/01/BBlintwo.png"),
            generate_carasol_items(
                "Quadratic Equations",
                "https://upload.wikimedia.org/wikipedia/en/thumb/e/e3/Quadratic-equation.svg/769px-Quadratic-equation.svg.png"),
            generate_carasol_items(
                "Basic Trignometry",
                "https://www.mathsisfun.com/images/adjacent-opposite-hypotenuse.gif")
        ])
    return response
