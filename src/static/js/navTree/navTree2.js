(function () {
  'use strict';

  const navTree = document.querySelector(`.navTree`);

  // slider functional
  const navTreeSlider = navTree.querySelector(`.navTree__slider`);
  const navTreeSliderArrow = navTree.querySelector(`.navTree__arrowSlider`);
  const navTreeList = navTree.querySelector(`.navTree__list`);

  const navTreeSliderClose = () => {
    navTreeSlider.removeEventListener(`click`, navTreeSliderClose);

    navTreeList.parentElement.classList.remove(`navTree--visible`);

    navTreeSlider.addEventListener(`click`, navTreeSliderOpen);
  };

  const navTreeSliderOpen = () => {
    navTreeSlider.removeEventListener(`click`, navTreeSliderOpen);

    navTreeList.parentElement.classList.add(`navTree--visible`);

    navTreeSlider.addEventListener(`click`, navTreeSliderClose);
  };

  navTreeSlider.addEventListener(`click`, navTreeSliderOpen);

}());

//# sourceMappingURL=navTree2.js.map
