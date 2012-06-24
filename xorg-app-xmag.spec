Summary:	xmag application
Summary(pl):	Aplikacja xmag
Name:		xorg-app-xmag
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xmag-%{version}.tar.bz2
# Source0-md5:	058d168d1c7c991b8d12158433ea5f63
Source1:	xmag.desktop
Source2:	xmag.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmag application.

%description -l pl
Aplikacja xmag.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xmag
%{_datadir}/X11/app-defaults/Xmag
%{_desktopdir}/xmag.desktop
%{_pixmapsdir}/xmag.png
%{_mandir}/man1/xmag.1x*
