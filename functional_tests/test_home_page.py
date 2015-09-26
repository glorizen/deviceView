from .base import FunctionalTest


# =============================================================================
# =============================================================================

class HomePageTest(FunctionalTest):

	def test_home_page(self):
	
		# I visit the home page.
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1280, 720)
		
		# I notice a mobile product on the page.
		self.assertTrue(self.browser.find_element_by_id('id_mobi_product'))