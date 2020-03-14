(function () {
  'use strict';

  const tabs = document.querySelectorAll(`.tabs__tab--second`);

  const removePrevActive = () => {
    tabs.forEach((tab) => {
      if (tab.classList.contains(`tabs__tab--second-active`)) {
        tab.classList.remove(`tabs__tab--second-active`);
      }
    });
  };

  const tabOnClick = (tab) => {
    removePrevActive();
    tab.classList.add(`tabs__tab--second-active`);
  };

  tabs.forEach((tab) => {
    tab.addEventListener(`click`, (evt) => {
      tabOnClick(evt.target);
    });
  });

  tabOnClick(tabs[0]);

}());

//# sourceMappingURL=tabs2.js.map
