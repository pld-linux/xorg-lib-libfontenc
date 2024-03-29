Summary:	fontenc - font encoding library
Summary(pl.UTF-8):	Biblioteka fontenc obsługująca kodowanie fontów
Name:		xorg-lib-libfontenc
Version:	1.1.8
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libfontenc-%{version}.tar.xz
# Source0-md5:	8816cc44d06ebe42e85950b368185826
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.70
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fontenc - font encoding library.

%description -l pl.UTF-8
Biblioteka fontenc obsługująca kodowanie fontów.

%package devel
Summary:	Header files for libfontenc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfontenc
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
# just for dirs
Requires:	xorg-proto-fontsproto-devel
Requires:	zlib-devel

%description devel
fontenc - font encoding library.

This package contains the header files needed to develop programs that
use libfontenc.

%description devel -l pl.UTF-8
Biblioteka fontenc obsługująca kodowanie fontów.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libfontenc.

%package static
Summary:	Static libfontenc library
Summary(pl.UTF-8):	Biblioteka statyczna libfontenc
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
fontenc - font encoding library.

This package contains the static libfontenc library.

%description static -l pl.UTF-8
Biblioteka fontenc obsługująca kodowanie fontów.

Pakiet zawiera statyczną bibliotekę libfontenc.

%prep
%setup -q -n libfontenc-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-encodingsdir=%{_fontsdir}/encodings

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfontenc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libfontenc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfontenc.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfontenc.so
%{_includedir}/X11/fonts/fontenc.h
%{_pkgconfigdir}/fontenc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfontenc.a
