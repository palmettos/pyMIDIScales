import re
import urllib
import mechanize

class Scraper:
	def __init__(self):
		self.browser = mechanize.Browser()
		self.root_url = 'http://www.scales-chords.com/'
		self.scale_info_url = 'scaleinfo.php'
		self.key_var = 'skey'
		self.scale_var = 'sname'
		self.query_vars = None
		self.query = '?'
		self.key_query = ''
		self.scale_query = ''
		self.goto = ''

	def _set_key(self, key):
		key = key.upper()
		if key == 'C#':
			key += '/Db'
		elif key == 'D#':
			key += '/Eb'
		elif key == 'F#':
			key += '/Gb'
		elif key == 'G#':
			key += '/Ab'
		elif key == 'A#':
			key += '/Bb'
		self.key_query = self.key_var+'='+urllib.quote(key)

	def _set_scale(self, scale):
		self.scale_query = self.scale_var+'='+scale

	def _build_query(self):
		self.query = '?'
		self.query_vars = []
		self.query_vars.append(self.key_query)
		self.query_vars.append(self.scale_query)
		for i in range(0, len(self.query_vars)):
			self.query += self.query_vars[i]
			if i < (len(self.query_vars)-1):
				self.query += '&'

	def _build_url(self):
		self.goto = self.root_url+self.scale_info_url+self.query

	def _search(self, key, scale):
		self._set_key(key)
		self._set_scale(scale)
		self._build_query()
		self._build_url()
		return self.browser.open(self.goto).read()

	def _get_scale_chord_links(self, key, scale):
		page = self._search(key, scale)
		pat = r'(\/showchord\.php\?ch=.*?)"'
		links = re.findall(pat, page)
		link_dict = {}
		for i in range(0, len(links)):
			pat = r'ch=(.*)'
			key = re.search(pat, links[i])
			links[i] = links[i].replace('\\\\', '\\')
			link_dict[key.group(1)] = links[i]
		return link_dict
		
	def get_scale_notes(self, key, scale):
		page = self._search(key, scale)
		pat = r'(\w#?\/?\w?\w?;)\s?'*7
		notes = re.search(pat, page)
		notes = re.sub(' ', '', notes.group(0))
		return notes.split(';')[:-1]

	def get_available_scales(self):
		nav_page = 'scalenav.php'
		page = self.browser.open(self.root_url+nav_page).read()
		pat = r'shscalesbytype\.php\?sname=(.*?)"'
		scales = re.findall(pat, page)
		return scales

	def get_scale_chords(self, key, scale):
		page = self._search(key, scale)
		pat = r'(\/showchord\.php\?ch=.*?)"'
		links = re.findall(pat, page)
		chords = []
		for i in range(0, len(links)):
			pat = r'ch=(.*)'
			key = re.search(pat, links[i])
			links[i] = links[i].replace('\\\\', '\\')
			links[i] = links[i].replace('%23', '#')
			chords.append(key.group(1))
		return chords

	def get_chord_notes(self, chord):
		if '#' in chord:
			chord = urllib.quote(chord)
		chord_link = 'showchord.php?ch='+chord
		url = self.root_url+chord_link
		page = self.browser.open(url).read()
		pat = r'Chord notes:\s?<\/td>\s?<td>\s?'+('(\wb?#?)?\s?'*6)
		notes = re.search(pat, page)
		count = 0
		for note in notes.groups():
			if note:
				count += 1
		return list(notes.groups())[0:count]

	def get_note_midi_value(self, note):
		notes = {
			'C': 60,
			'C#': 61,
			'Db': 61,
			'D': 62,
			'D#': 63,
			'Eb': 63,
			'E': 64,
			'F': 65,
			'F#': 66,
			'Gb': 66,
			'G': 67,
			'G#': 68,
			'Ab': 68,
			'A': 69,
			'A#': 70,
			'Bb': 70,
			'B': 71
		}
		return notes[note]