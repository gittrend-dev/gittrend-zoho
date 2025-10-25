def generate_html(repos):
    html = "<h2>Top Trending GitHub Repos</h2><ul>"
    for r in repos:
        html += f'<li><a href="{r["url"]}">{r["author"]}/{r["name"]}</a> - {r["language"]} ⭐ {r["stars"]}</li>'
    html += "</ul>"
    return html
