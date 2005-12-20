Summary:	fontenc library
Summary(pl):	Biblioteka fontenc
Name:		xorg-lib-libfontenc
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/lib/libfontenc-%{version}.tar.bz2
# Source0-md5:	c0eff6b88213629cb72ca9c4486900a4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fontenc library.

%description -l pl
Biblioteka fontenc.

%package devel
Summary:	Header files for libfontenc library
Summary(pl):	Pliki nag³ówkowe biblioteki libfontenc
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
# just for dirs
Requires:	xorg-proto-fontsproto-devel
Requires:	zlib-devel

%description devel
fontenc library.

This package contains the header files needed to develop programs that
use libfontenc.

%description devel -l pl
Biblioteka fontenc.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libfontenc.

%package static
Summary:	Static libfontenc library
Summary(pl):	Biblioteka statyczna libfontenc
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
fontenc library.

This package contains the static libfontenc library.

%description static -l pl
Biblioteka fontenc.

Pakiet zawiera statyczn± bibliotekê libfontenc.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libfontenc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfontenc.so
%{_libdir}/libfontenc.la
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/fontenc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfontenc.a
