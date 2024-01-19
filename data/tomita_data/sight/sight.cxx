#encoding "utf-8"    // сообщаем парсеру о том, в какой кодировке написана грамматика

Name -> Word<kwtype=sight>;

Sight -> Name interp (Sight.Name::norm="nom,sg");
//Sight -> Name interp (Sight.Name);
