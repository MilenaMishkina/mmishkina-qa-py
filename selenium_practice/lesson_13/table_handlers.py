from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class TableHandler:
    TABLE_LOCATOR = ('xpath', '//table')
    ROWS_LOCATOR = ('xpath', '//tr')
    CELLS_LOCATOR = ('xpath', './/td|.//th')
    HEAD_CELLS_LOCATOR = ('xpath', '//th')
    # Если указать локатор вот так './/tr', то точка означает,что поиск относитально чего-то.
    # Это нужно, если несколько таблиц с одинаковыми названиями и нам в find_element нужно искать относительно конкретной таблицы

    def __init__(self, driver:WebDriver):
        self.driver = driver

    @property
    def _table(self) -> WebElement:
        return self.driver.find_element(*self.TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self.ROWS_LOCATOR)

    # Получение контента ячейки
    def get_cell_content(self, row_number, column_number):
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self.CELLS_LOCATOR)[column_number - 1]
        return cell.text

    # Получение контента всего ряда
    def get_row_content(self, row_number) -> list:
        row = self._rows[row_number - 1]
        return [cell.text for cell in row.find_elements(*self.CELLS_LOCATOR)]

    # Получение контента всей колонки
    def get_column_content(self, column_number):
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self.CELLS_LOCATOR)
            column_content.append(cells[column_number - 1].text)
        return column_content

    # Поиск записи по признаку (в данном случае - по году)
    def find_film_by_year(self, row_number, column_number):
        if "1999" in self.get_cell_content(row_number, column_number):
            return f'Film of this year is {self.get_cell_content(row_number, column_number - 1)}'
        else:
            return f'This is - {self.get_cell_content(row_number, column_number)} is not film 1999'
