Summary:	fontenc library
Summary(pl):	Biblioteka fontenc
Name:		xorg-lib-libfontenc
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libfontenc-%{version}.tar.bz2
# Source0-md5:	a26b8f108a99ab48f3d01ffdcda2725d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
fontenc library.

%description -l pl
Biblioteka fontenc.

%package devel
Summary:	Header files libfontenc development
Summary(pl):	Pliki nag³ówkowe do biblioteki libfontenc
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Requires:	zlib-devel

%description devel
fontenc library.

This package contains the header files needed to develop programs that
use these libfontenc.

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
%configure

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
