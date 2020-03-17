(function () {
  'use strict';

  const navTree = document.querySelector(`.navTree`);
  const navTreeItems = navTree.querySelectorAll(`.navTree__item`);

  const listSearch = (element) => {
    if (element.parentNode.querySelector(`.navTree__list`)) {
      return true;
    }
    return false;
  };

  const setActiveNavItemFirst = (navItems, target) => {
    const parent = target.closest(`.navTree__item--first`);
    navItems.forEach((navItem) => {
      navItem.classList.remove(`navTree__item--first-active`);
      const prevActive = navItem.querySelector(`.navTree__firstLevel--active`);
      if (prevActive) {
        prevActive.classList.remove(`navTree__firstLevel--active`);
        prevActive.firstElementChild.classList.remove(`navTree__arrow--dropped`);
      }
    });
    parent.classList.add(`navTree__item--first-active`);
    target.classList.add(`navTree__firstLevel--active`);
    target.firstElementChild.classList.add(`navTree__arrow--dropped`);
  };

  const setActiveNavItemSecond = (navItems, target) => {
    const parent = target.closest(`.navTree__item--second`);
    navItems.forEach((navItem) => {
      navItem.classList.remove(`navTree__item--second-active`);
      const prevActive = navItem.querySelector(`.navTree__secondLevel--active`);
      if (prevActive) {
        prevActive.classList.remove(`navTree__secondLevel--active`);
        prevActive.firstElementChild.classList.remove(`navTree__arrow--dropped`);
      }
    });
    parent.classList.add(`navTree__item--second-active`);
    target.classList.add(`navTree__secondLevel--active`);
    target.firstElementChild.classList.add(`navTree__arrow--dropped`);
  };

  const navTreeItemOnClick = (evt) => {
    evt.preventDefault();

    if (listSearch(evt.target) && evt.target.classList.contains(`navTree__firstLevel`)) {
      setActiveNavItemFirst(navTreeItems, evt.target);
    }
    if (listSearch(evt.target) && evt.target.classList.contains(`navTree__secondLevel`)) {
      setActiveNavItemSecond(navTreeItems, evt.target);
    }
  };

  navTreeItems.forEach((item) => {
    item.addEventListener(`click`, navTreeItemOnClick);
  });

}());

//# sourceMappingURL=navTree.js.map
