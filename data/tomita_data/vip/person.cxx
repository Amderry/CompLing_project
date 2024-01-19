#encoding "utf-8"    // сообщаем парсеру о том, в какой кодировке написана грамматика

Name -> Word<kwtype="имя">;
SName -> Word<kwtype="фамилия">;

// Андрей Бочаров
VipPerson -> Name interp (VipPerson.Name)
             SName interp (VipPerson.SName);

// Бочаров Андрей
VipPerson -> SName interp (VipPerson.SName)
	     Name interp (VipPerson.Name);
             
// Бочаров
VipPerson -> SName interp (VipPerson.SName);
