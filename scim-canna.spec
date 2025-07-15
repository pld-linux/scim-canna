Summary:	SCIM IMEngine module using Canna for Japanese input
Summary(pl.UTF-8):	Silnik IM SCIM dla metody wprowadzania znaków japońskich Canna
Name:		scim-canna
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://osdn.jp/projects/scim-imengine/releases/p3528
Source0:	http://dl.osdn.jp/scim-imengine/29155/%{name}-%{version}.tar.gz
# Source0-md5:	41bf2796c95689df740be07922c74f67
Patch0:		%{name}-no-rpath.patch
Patch1:		%{name}-gtk3.patch
URL:		https://osdn.jp/projects/scim-imengine/
BuildRequires:	Canna-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.0
Requires:	Canna
Requires:	scim >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scim-canna is a SCIM IMEngine module using Canna.

Canna is a traditional Japanese conversion engine on UNIX like system.
It converts key events to Kana Kanji mixed text.

%description -l pl.UTF-8
scim-canna to moduł silnika IM SCIM wykorzystujący metodę Canna.

Cana to tradycyjny silnik konwersji języka japońskiego na systemach
uniksowych. Zamienia zdarzenia klawiszy na mieszany tekst Kana Kanji.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/canna.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/canna-imengine-setup.so
%{_datadir}/scim/icons/scim-canna.png
