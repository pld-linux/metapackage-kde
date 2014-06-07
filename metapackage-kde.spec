Summary:	KDE metapackage
Summary(pl.UTF-8):	Metapakiet KDE
Name:		metapackage-kde
Version:	3.5
Release:	0.4
License:	Freeware
Group:		Applications/System
Requires:	X11-OpenGL-libGL
Requires:	giflib
Requires:	hicolor-icon-theme
Requires:	kde-kgreet-classic
Requires:	kde-kgreet-winbind
#Requires:	kde-logoutpic-PLD
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package to build up KDE desktop environment.

%description -l pl.UTF-8
Pakiet tworzący środowisko graficzne KDE.

%package kdebase
Summary:	kdebase metapackage
Group:		Applications/System
Requires:	kde-decoration-b2 >= %{version}
Requires:	kde-decoration-keramik >= %{version}
Requires:	kde-decoration-laptop >= %{version}
Requires:	kde-decoration-modernsys >= %{version}
Requires:	kde-decoration-quartz >= %{version}
Requires:	kde-decoration-redmond >= %{version}
Requires:	kde-decoration-web >= %{version}
Requires:	kde-kio-ldap >= %{version}
Requires:	kde-kio-nntp >= %{version}
Requires:	kde-kio-pop3 >= %{version}
Requires:	kde-kio-smtp >= %{version}
Requires:	kde-kside-default >= %{version}
Requires:	kdebase-common-filemanagement >= %{version}
Requires:	kdebase-common-konsole >= %{version}
Requires:	kdebase-core >= %{version}
Requires:	kdebase-desktop >= %{version}
Requires:	kdebase-infocenter >= %{version}
Requires:	kdebase-kappfinder >= %{version}
Requires:	kdebase-kate >= %{version}
Requires:	kdebase-kdcop >= %{version}
Requires:	kdebase-kdeprintfax >= %{version}
Requires:	kdebase-kdialog >= %{version}
Requires:	kdebase-kfind >= %{version}
Requires:	kdebase-kfontinst >= %{version}
Requires:	kdebase-kjobviewer >= %{version}
Requires:	kdebase-klipper >= %{version}
Requires:	kdebase-konsole >= %{version}
Requires:	kdebase-kpager >= %{version}
Requires:	kdebase-kpersonalizer >= %{version}
Requires:	kdebase-ksysguard >= %{version}
Requires:	kdebase-kwrite >= %{version}
Requires:	kdebase-kwrited >= %{version}
Requires:	kdebase-libkate >= %{version}
Requires:	kdebase-libksgrd >= %{version}
Requires:	kdebase-screensavers >= %{version}
Requires:	kdebase-useraccount >= %{version}
Requires:	konqueror >= %{version}
Requires:	konqueror-libs >= %{version}

%description kdebase
kdebase metapackage

%package kmail
Summary:	kmail metapackage
Summary(pl.UTF-8):	Metapakiet kmail
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

%description kmail
kmail metapackage.

%description kmail -l pl.UTF-8
Metapakiet kmail.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files kdebase
%defattr(644,root,root,755)

%files kmail
%defattr(644,root,root,755)
