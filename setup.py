

from distutils.core import setup

setup(
	name = 'p2psip',
	version = '2.2.3',
	description = '39 Peers: Opensource peer-to-peer Internet telephony (P2P-SIP) software in Python',
	author = 'Kundan Singh',
	author_email = 'kundan10@gmail.com',
	url = 'http://39peers.net',
	license = 'GPL v3',
	packages = ['p2psip', 'p2psip.app', 'p2psip.external', 'p2psip.std', 'p2psip.std.w3c', 'p2psip.tools' ],
	data_files = [('', [ 'LICENSING', 'README.md' ])]
)
