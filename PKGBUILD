# Script generated with Bloom
pkgdesc="ROS - The pr2_mechanism stack contains the infrastructure to control the PR2 robot in a hard realtime control loop."
url='http://ros.org/wiki/pr2_mechanism'

pkgname='ros-kinetic-pr2-mechanism'
pkgver='1.8.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-pr2-controller-interface'
'ros-kinetic-pr2-controller-manager'
'ros-kinetic-pr2-hardware-interface'
'ros-kinetic-pr2-mechanism-diagnostics'
'ros-kinetic-pr2-mechanism-model'
)

conflicts=()
replaces=()

_dir=pr2_mechanism
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_mechanism $srcdir/pr2_mechanism
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

