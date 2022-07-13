Summary:	xmag application to magnify parts of the screem
Summary(pl.UTF-8):	Aplikacja xmag powiększająca kawałki ekranu
Name:		xorg-app-xmag
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xmag-%{version}.tar.xz
# Source0-md5:	c73f20334a36879868b4f6ced17b1ead
Source1:	xmag.desktop
Source2:	xmag.png
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xmag program allows you to magnify portions of an X screen.

%description -l pl.UTF-8
Aplikacja xmag pozwala powiększać części ekranu X.

%prep
%setup -q -n xmag-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xmag.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xmag.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xmag
%{_datadir}/X11/app-defaults/Xmag
%{_desktopdir}/xmag.desktop
%{_pixmapsdir}/xmag.png
%{_mandir}/man1/xmag.1*
