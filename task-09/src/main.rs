use scraper::{Html, Selector};

fn main() {
    let url = "https://crypto.com/price";
    let respone = reqwest::blocking::get(url).unwrap();
    let body = respone.text().unwrap();
    let document = Html::parse_document(&body);
    let row_selector = Selector::parse("tbody>tr").unwrap();
    let name_selector = Selector::parse("p.chakra-text.css-rkws3").unwrap();   
    let price_selector = Selector::parse("td div.css-0").unwrap();
    let change_selector = Selector::parse("td.css-1b7j986 p").unwrap();
    let volume_selector = Selector::parse("td.css-1nh9lk8").unwrap();
    let marketcap_selector = Selector::parse("td.css-1nh9lk8~td").unwrap();
    let mut wtr = csv::Writer::from_path("crypto.csv").unwrap();
    wtr.write_record(&["Name","Price","24HR Change","24hr Volume","Market Cap"]).unwrap();
    
    for rows in document.select(&row_selector){
        let name = rows.select(&name_selector).next().unwrap().text().collect::<String>();
        let price = rows.select(&price_selector).next().unwrap().text().collect::<String>();
        let change = rows.select(&change_selector).next().unwrap().text().collect::<String>();
        let volume = rows.select(&volume_selector).next().unwrap().text().collect::<String>();
        let marketcap = rows.select(&marketcap_selector).next().unwrap().text().collect::<String>();
        wtr.write_record([name,price,change,volume,marketcap]).unwrap();
    }


}
   
