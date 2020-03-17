(function () {
  'use strict';

  const navTopItems = document.querySelectorAll(`.navTop__item:not(.navTop__item--vr)`);

  const navTopItemOnMouseOver = (evt) => {
    
  };

  navTopItems.forEach((item) => {
    item.addEventListener(`mouseover`, navTopItemOnMouseOver);
  });

}());

//# sourceMappingURL=navTop.js.map
