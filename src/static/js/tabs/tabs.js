(function () {
  'use strict';

  const tabs = document.querySelector(`.tabs`);
  const tabsFirst = tabs.querySelectorAll(`.tabs__tab--first`);
  const tabsContentFirst = tabs.querySelectorAll(`.tabs__tabContent--first`);

  const searchAllTabs = (content, contentIndex) => {
    const tabsSecond = content.querySelectorAll(`.tabs__tab--second`);
    const tabsContentSecond = tabsContentFirst[contentIndex].querySelectorAll(`.tabs__tabContent--second`);
    tabsSecond.forEach((tab, index) => {
      tab.addEventListener(`click`, () => {
        tabSecondEventListner(tabsSecond, index, tabsContentSecond);
      });
    
    });
  };

  const setActiveTabFirst = (tabs, index) => {
    tabs.forEach((tab) => {
      tab.classList.remove(`tabs__tab--active`);
    });
    tabs[index].classList.add(`tabs__tab--active`);
  };

  const setActiveTabSecond = (tabs, index) => {
    tabs.forEach((tab) => {
      tab.classList.remove(`tabs__tab--second-active`);
    });
    tabs[index].classList.add(`tabs__tab--second-active`);
  };

  const setActiveTabContent = (tabsContent, index) => {
    // console.log(tabsContent);
    
    tabsContent.forEach((tabContent) => {
      tabContent.classList.remove(`tabs__tabContent--active`);
    });
    tabsContent[index].classList.add(`tabs__tabContent--active`);
  };

  const tabFirstEventListner = (tabs, index, content) => {
    setActiveTabFirst(tabs, index);
    setActiveTabContent(content, index);
  };

  const tabSecondEventListner = (tabs, index, content) => {
    setActiveTabSecond(tabs, index);
    setActiveTabContent(content, index);
  };

  tabsFirst.forEach((tab, index) => {
    tab.addEventListener(`click`, () => {
      // console.log(`tab ${index} first level click`);
      tabFirstEventListner(tabsFirst, index, tabsContentFirst);
    });

  });

  tabsContentFirst.forEach((content, index) => {
    searchAllTabs(content, index);
  });

}());

//# sourceMappingURL=tabs.js.map
