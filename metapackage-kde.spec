Summary:	KDE
Name:		role-kde
Version:	3.5
Release:	0.1
License:	Freeware
Group:		Applications/System
Obsoletes:	role-kde
Requires:	X11-OpenGL-libGL
Requires:	giflib
Requires:	hicolor-icon-theme
Requires:	kde-kgreet-classic
Requires:	kde-kgreet-winbind
Requires:	kde-logoutpic-PLD
Requires:	kde-splashplugin-Standard
Requires:	kdeaddons-ark
Requires:	kdeaddons-fsview
Requires:	kdeaddons-kate
Requires:	kdeaddons-konqueror
Requires:	kdeaddons-lnkforward
Requires:	kdeartwork-screensavers
Requires:	kdeartwork-sounds
Requires:	kdeartwork-wallpapers
Requires:	kdebase-desktop
Requires:	kdebase-konsole
Requires:	kdegraphics-kamera
Requires:	kdegraphics-kghostview
Requires:	kdegraphics-kiconedit
Requires:	kdegraphics-kolourpaint
Requires:	kdegraphics-kpdf
Requires:	kdegraphics-ksnapshot
Requires:	kdegraphics-kuickshow
Requires:	kdegraphics-kview
Requires:	kdemultimedia-audiocd
Requires:	kdemultimedia-kmix
Requires:	kdemultimedia-krec
Requires:	kdenetwork-kopete
Requires:	kdenetwork-kopete-protocol-icq
Requires:	kdenetwork-kopete-protocol-jabber
Requires:	kdenetwork-kopete-protocol-msn
Requires:	kdenetwork-kopete-tool-cryptography
Requires:	kdenetwork-kopete-tool-history
Requires:	kdenetwork-krfb
Requires:	kdenetwork-ksirc
Requires:	kdenetwork-lanbrowser
Requires:	kdenetwork-rss
Requires:	kdeutils-kcalc
Requires:	kdeutils-kcharselect
Requires:	kdeutils-kdessh
Requires:	kdeutils-kgpg
Requires:	kdeutils-kwalletmanager
Requires:	konqueror
Requires:	role-X11-fonts
%ifnarch %{x8664}
Requires:	macromedia-flash
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%prep

%description
Package to build up KDE desktop environment.

%package -n role-kmail
Summary:	kmail
Group:		Applications/Mail
Requires:	cyrus-sasl
Requires:	cyrus-sasl-cram-md5
Requires:	cyrus-sasl-digest-md5
Requires:	cyrus-sasl-login
Requires:	cyrus-sasl-plain
Requires:	gnupg-agent
Requires:	gnupg-smime
Requires:	gnupg2
Requires:	kde-kio-ldap
Requires:	kdepim
Requires:	kdepim-kaddressbook
Requires:	kdepim-kmail
Requires:	keychain >= 2.5.0
Requires:	pinentry-qt
Obsoletes:	role-kde-kmail

%description -n role-kmail

%package -n role-X11
Summary:	X11
Group:		Applications/Mail
Requires:	X11-Xserver
Obsoletes:	role-kde-X11

%description -n role-X11

%package -n role-X11-fonts
Summary:	fonts
Group:		Applications/Mail
Requires:	fonts-TTF-bitstream-vera
Requires:	fonts-TTF-microsoft
Requires:	fonts-TTF-microsoft-tahoma
Requires:	role-X11
Obsoletes:	role-fonts
Obsoletes:	role-kde-fonts

#X11-fonts
#X11-fonts-75dpi
#X11-fonts-75dpi-ISO8859-1
#X11-fonts-75dpi-ISO8859-10
#X11-fonts-75dpi-ISO8859-13
#X11-fonts-75dpi-ISO8859-14
#X11-fonts-75dpi-ISO8859-15
#X11-fonts-75dpi-ISO8859-2
#X11-fonts-75dpi-ISO8859-3
#X11-fonts-75dpi-ISO8859-4
#X11-fonts-75dpi-ISO8859-9
#X11-fonts-ISO8859-1
#X11-fonts-ISO8859-2
#X11-fonts-ISO8859-3
#X11-fonts-KOI8-R

%description -n role-X11-fonts

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n role-kmail
%defattr(644,root,root,755)

%files -n role-X11
%defattr(644,root,root,755)

%files -n role-X11-fonts
%defattr(644,root,root,755)
