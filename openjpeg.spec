# NOTE: for openjpeg 2.x see openjpeg2.spec
Summary:	An open-source JPEG 2000 codec
Summary(pl.UTF-8):	Biblioteka kodująca i dekodująca format JPEG 2000
Name:		openjpeg
Version:	1.5.1
Release:	2
License:	BSD
Group:		Libraries
#Source0Download: http://code.google.com/p/openjpeg/downloads/list
Source0:	http://openjpeg.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	b5f74cec2688fb918331bb014061be6f
Patch0:		%{name}-opt.patch
URL:		http://www.openjpeg.org/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenJPEG library is an open-source JPEG 2000 codec written in C
language. It has been developed in order to promote the use of JPEG
2000, the new still-image compression standard from the Joint
Photographic Experts Group (JPEG).

%description -l pl.UTF-8
OpenJPEG to mająca otwarte źródła biblioteka kodująca i dekodująca
format JPEG 2000, napisana w języku C. Powstała w celu promowania
użycia formatu JPEG 2000 - nowego standardu obrazów nieruchomych
stworzonego przez grupę JPEG (Joint Photographic Experts Group).

%package devel
Summary:	Header file for OpenJPEG library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki OpenJPEG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header file needed for developing programs
using the OpenJPEG library.

%description devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy potrzebny do tworzenia programów
wykorzystujących bibliotekę OpenJPEG.

%package static
Summary:	Static OpenJPEG library
Summary(pl.UTF-8):	Statyczna biblioteka OpenJPEG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenJPEG library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenJPEG.

%package progs
Summary:	OpenJPEG codec programs
Summary(pl.UTF-8):	Programy kodujące/dekodujące dla biblioteki OpenJPEG
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
OpenJPEG codec programs.

%description progs -l pl.UTF-8
Programy kodujące/dekodujące dla biblioteki OpenJPEG.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-jpwl \
	--enable-mj2
# no --enable-jpip here (see openjpip.spec for it)

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libopenjpeg*.la
# packaged as doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/openjpeg-1.5

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE NEWS README THANKS
%attr(755,root,root) %{_libdir}/libopenjpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenjpeg.so.1
%attr(755,root,root) %{_libdir}/libopenjpeg_JPWL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenjpeg_JPWL.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenjpeg.so
%attr(755,root,root) %{_libdir}/libopenjpeg_JPWL.so
%{_includedir}/openjpeg-1.5
%{_pkgconfigdir}/libopenjpeg1.pc
%{_pkgconfigdir}/libopenjpeg.pc
%{_pkgconfigdir}/libopenjpeg-jpwl.pc
%{_mandir}/man3/jpwl_libopenjpeg.3*
%{_mandir}/man3/libopenjpeg.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenjpeg.a
%{_libdir}/libopenjpeg_JPWL.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/JPWL_image_to_j2k
%attr(755,root,root) %{_bindir}/JPWL_j2k_to_image
%attr(755,root,root) %{_bindir}/extract_j2k_from_mj2
%attr(755,root,root) %{_bindir}/frames_to_mj2
%attr(755,root,root) %{_bindir}/image_to_j2k
%attr(755,root,root) %{_bindir}/j2k_dump
%attr(755,root,root) %{_bindir}/j2k_to_image
%attr(755,root,root) %{_bindir}/mj2_to_frames
%attr(755,root,root) %{_bindir}/wrap_j2k_in_mj2
%{_mandir}/man1/jpwl_image_to_j2k.1*
%{_mandir}/man1/jpwl_j2k_to_image.1*
%{_mandir}/man1/image_to_j2k.1*
%{_mandir}/man1/j2k_dump.1*
%{_mandir}/man1/j2k_to_image.1*
