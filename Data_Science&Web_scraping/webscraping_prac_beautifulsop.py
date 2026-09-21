for item in items:
    title_tag = item.find("div", class_="ucw-widget-product-card-title") or \
                item.find("span", class_="ucw-widget-product-card-title")
    price_tag = item.find("div", class_="ucw-widget-product-card-price") or \
                item.find("span", class_="ucw-widget-product-card-price")

    title = title_tag.get_text(strip=True) if title_tag else None

    price = None
    if price_tag:
        price_text = price_tag.get_text(strip=True)
        match = re.search(r'PKR\s?[\d,]+\.\d{2}', price_text)
        price = match.group() if match else price_text

    # NAYA link-finding logic
    link = None
    all_links = item.find_all("a", href=True)
    for a in all_links:
        href = a["href"]
        if "/dp/" in href or "/gp/product/" in href:
            link = href
            if link.startswith("/"):
                link = "https://www.amazon.com" + link
            break

    if title:
        products.append({"title": title, "price": price, "link": link})