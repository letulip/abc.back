(function () {
  'use strict';

  const folder = document.querySelector(`.folder`);
  const folderHeadings = folder.querySelectorAll(`.folder__heading`);

  const folderHeadingOnClick = (evt) => {
    const files = folder.querySelectorAll(`.folder__file`);
    files.forEach((file) => {
      const dropdownIcon = file.querySelector(`.folder__dropdownIcon--dropped`);
      if (dropdownIcon) {
        dropdownIcon.classList.remove(`folder__dropdownIcon--dropped`);
      }

      const dropdown = folder.querySelector(`.dropdown--visible`);
      if (dropdown) {
        dropdown.classList.remove(`dropdown--visible`);
      }
    });

    const targetDropdown = evt.target.querySelector(`.folder__dropdownIcon`);
    targetDropdown.classList.add(`folder__dropdownIcon--dropped`);
    const dropdown = evt.target.nextElementSibling;
    dropdown.classList.add(`dropdown--visible`);
  };

  folderHeadings.forEach((heading) => {
    heading.addEventListener(`click`, (evt) => {
      folderHeadingOnClick(evt);
    });
  });

}());

//# sourceMappingURL=sponki.js.map
